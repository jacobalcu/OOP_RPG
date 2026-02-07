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

    def _process_input(self):
        # Get user intent
        command = input(
            "What direction do you want to go? (north, south, east, west, or quit) "
        ).lower()

        if not command:
            return

        if command == "quit":
            self.is_running = False
        else:
            self._handle_move(command)

    def _handle_take(self, item_name):
        # try to get item object from room
        item_object = self.player.current_room.remove_item(item_name)
        if item_object:
            self.player.pick_up(item_object)
            print(f"You took the {item_object.name}")
        else:
            print(f"There is no {item_name} here")

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

    def start(self):
        # Game Loop
        print("Welcome to the Dungeon Game")

        while self.is_running:

            # Display state
            current_room = self.player.current_room
            print(f"You are in {current_room.get_description()}")

            # Get Input
            self._process_input()

        print("Thanks for playing!")
