# Import Room and Player to build world
from world import Room
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
        for _ in range(depth):
            new_room = RandomRoomFactory.generate_random_room()

            # Connect
            last_room.set_exit("north", new_room)

            # Move pointer
            last_room = new_room
        return entrance

    def _setup_game(self):
        # Architect: Create and Connect objects
        # Create Rooms
        # hallway = Room("a dim, stone-walled hallway.")
        # kitchen = Room("a kitchen smelling of old herbs.")
        # armory = Room("a dusty room filled with rusted swords")

        # Connect Rooms
        # hallway.set_exit("north", kitchen)
        # hallway.set_exit("east", armory)

        # kitchen.set_exit("south", hallway)
        # armory.set_exit("west", hallway)

        entrance = self._generate_linear_dungeon(10)

        # Create Player and place in "Start Room"
        # Dependency Injection: passing Room obj to Player
        self.player = Player("Hero", entrance)

    def _process_input(self):
        # Get user intent
        command = input(
            "\nWhat direction do you want to go? (north, south, east, west, or quit) "
        ).lower()

        if not command:
            return

        if command == "quit":
            self.is_running = False
        else:
            success = self.player.move(command)
            if not success:
                print("You run into a wall. No exit that way.")

    def start(self):
        # Game Loop
        print("Welcome to the Dungeon Game")

        while self.is_running:
            # Display state
            current_room = self.player.current_room
            print(f"\nYou are in {current_room.get_description()}")

            # Get Input
            self._process_input()

        print("Thanks for playing!")
