from world import Room
import random


class RoomFactory:
    # staticmethod bc the class doesn't store any data
    # just call RoomFactory.create_room()
    @staticmethod
    def create_room(room_type):
        """
        A centralized place to define room types
        """
        if room_type == "forest":
            return Room("a lush green forest with sunlight filtering through leaves.")
        elif room_type == "dungeon":
            return Room("a cold, damp dungeon cell with iron bars.")
        elif room_type == "treasure":
            # You could even return a special 'TreasureRoom' subclass here later!
            return Room("a glittering chamber filled with gold coins.")
        else:
            return Room("a generic, featureless stone room.")


class RandomRoomFactory:
    _themes = ["Spooky", "Volcanic", "Frozen", "Overgrown"]

    # method belongs to this Class, not a specific object
    @classmethod
    def generate_random_room(cls):
        theme = random.choice(cls._themes)
        return Room(f"a {theme} chamber that feels dangerous.")
