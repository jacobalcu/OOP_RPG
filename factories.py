from world import Room
from items import Item, Key
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

    # @staticmethod
    # def create_treasure_room():
    #     room = Room("a sparkling treasury")
    #     gold_key = Key(
    #         "Gold Key", "A heavy, ornate key made of solid gold.", "main_gate"
    #     )
    #     room.add_item(gold_key)
    #     return room

    @staticmethod
    def create_basic_dungeon():
        """Creates a standard, pre-defined 3-room layout."""
        hallway = Room("a dim, stone-walled hallway.")
        kitchen = Room("a kitchen smelling of old herbs.")
        vault = Room("a heavy steel vault.", is_locked=True, lock_id="vault_key_01")

        # Adding items manually for fixed layouts
        hallway.add_item(Item("Stone", "A smooth, cold pebble."))
        kitchen.add_item(Key("Rusty Key", "A jagged iron key.", "vault_key_01"))

        # Linking
        hallway.set_exit("north", kitchen)
        hallway.set_exit("east", vault)

        return hallway  # Return the starting point

    @classmethod
    def create_random_room(cls):
        """Generates a room with random flavor and a chance for items."""
        themes = ["Overgrown", "Frozen", "Volcanic", "Empty"]
        chosen_theme = random.choice(themes)

        room = Room(f"a {chosen_theme} chamber.")

        # Logic: 30% chance to contain a random generic item
        if random.random() < 0.3:
            room.add_item(cls._generate_random_loot())

        return room

    @staticmethod
    def _generate_random_loot():
        # helper func
        loot_pool = [
            ("Old Bone", "It looks human. Best not to think about it."),
            ("Dusty Note", "It says: 'The gold is in the north'"),
            ("Empty Bottle", "Smells like cheap ale."),
        ]
        name, desc = random.choice(loot_pool)
        return Item(name, desc)


class RandomRoomFactory:
    _themes = ["Spooky", "Volcanic", "Frozen", "Overgrown"]

    # method belongs to this Class, not a specific object
    @classmethod
    def generate_random_room(cls):
        theme = random.choice(cls._themes)
        return Room(f"a {theme} chamber that feels dangerous.")
