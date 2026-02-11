# Import Room and Player to build world
from world import Room
from items import Key
from factories import RoomFactory, RandomRoomFactory
from entities import Player


# Define Game Class
class Game:
    def __init__(self):
        self.player = None
        self.is_running = True
        # Setup world immediately upon creation
        self._setup_game()

    # def _handle_command(self, command_str):
    #     # Parse command and execute
    #     parts = command_str.split()
    #     if not parts:
    #         return

    #     verb = parts[0].lower()
    #     if verb in ["go", "move"]:
    #         if len(parts) < 2:
    #             print("Take what?")
    #             return

    #         item_name = " ".join(parts[1:])
    #         item_obj = self.player.current_room.remove_item(item_name)

    #         if item_obj:
    #             self.player.pick_up(item_obj)
    #             print(f"You pick up the {item_obj.name}")
    #         else:
    #             print(f"There is no {item_name} here.")
    #     elif verb in ["inventory", "i"]:
    #         print(self.player.get_inventory())

    def _generate_linear_dungeon(self, depth):
        # Create entrance using factory
        entrance = RoomFactory.create_room("dungeon")
        last_room = entrance

        # Build the chain of rooms
        for i in range(depth):
            new_room = RandomRoomFactory.generate_random_room()
            if i == 3:
                new_room.is_locked = True

            # Connect
            last_room.set_exit("north", new_room)

            # Move pointer
            last_room = new_room
        return entrance

    def _setup_game(self):
        # Architect: Create and Connect objects
        # entrance = self._generate_linear_dungeon(10)
        self.start_room = RoomFactory.create_basic_dungeon()
        self.player = Player("Hero", self.start_room)

        # Create Player and place in "Start Room"
        # Dependency Injection: passing Room obj to Player
        # self.player = Player("Hero", entrance)

    # def _process_input(self):
    #     # Get user intent
    #     command = input(
    #         "What direction do you want to go? (north, south, east, west, or quit) "
    #     ).lower()

    #     if not command:
    #         return

    #     if command == "quit":
    #         self.is_running = False
    #     else:
    #         self._handle_move(command)

    def _handle_take(self, item_name):
        if not item_name:
            print("Take what?")
            return

        item_object = self.player.current_room.remove_item(item_name)

        # try to get item object from room
        if item_object:
            self.player.pick_up(item_object)
            print(f"You took the {item_object.name}")
        else:
            print(f"There is no {item_name} here")

    def _handle_use(self, item_name):
        if not item_name:
            print("Use what?")
            return

        # Find item in inventory
        item_object = self.player.get_item_from_inventory(item_name)

        if not item_object:
            print(f"You don't have a {item_name}")
            return

        # Polymorphism: Check what kind of item
        if isinstance(item_object, Key):
            self._handle_unlock(item_object)
        else:
            print(f"You can't use the {item_object.name} right now.")

    def _handle_unlock(self, key_object):
        # Check all exits in current room
        for direction, room in self.player.current_room.get_all_exits().items():
            if room.is_locked and room.lock_id == key_object.lock_id:
                print(
                    f"You unlock the door to the {direction} using the {key_object.name}"
                )
                room.is_locked = False
                return

        print("There is nothing to unlock here with that key.")

    def _handle_move(self, direction):
        result = self.player.move(direction)

        if result == "success":
            print(f"You move {direction}.")
        elif result == "wall":
            print("You run into a wall. No exit that way.")
        elif result == "locked":
            targetRoom = self.player.current_room.get_exit(direction)
            can_open = False
            # Logic 'bridge' between Player and Room
            for item in self.player.get_inventory():
                if isinstance(item, Key) and item.lock_id == targetRoom.lock_id:
                    can_open = True
                    break
            if can_open:
                # Reach into next room and unlock it
                print(f"You unlock the door using the {item.name}")
                targetRoom.is_locked = False
                # Repeat move
                self.player.move(direction)
            else:
                print("The door is locked. You need a key")

    def _process_command(self, user_input):
        parts = user_input.split()
        if not parts:
            return

        verb = parts[0]
        noun = " ".join(parts[1:]) if len(parts) > 1 else None

        if verb == "quit":
            self.is_running = False
        elif verb == "go":
            self._handle_move(noun)
        elif verb in ["take", "get"]:
            self._handle_take(noun)
        elif verb in ["inventory", "i"]:
            print(self.player.get_inventory())
        elif verb == "use":
            self._handle_use(noun)
        else:
            print("Unknown command. Try 'go', 'take', 'inventory', or 'quit'.")

    def start(self):
        # Game Loop
        print("Welcome to the Dungeon Game")

        while self.is_running:

            # Display state
            current_room = self.player.current_room
            print(f"You are in {current_room.get_description()}")

            # Get input
            user_input = input("\n> ").strip().lower()

            # Get Input
            # self._process_input()
            self._process_command(user_input)

        print("Thanks for playing!")
