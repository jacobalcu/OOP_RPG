# Define Player here
class Player:
    def __init__(self, name, cur_room):
        self._curRoom = cur_room
        self._name = name
        self._inventory = ["key"]

    @property
    def name(self):
        # Return player's name
        return self._name

    @property
    def current_room(self):
        # Return player's current room
        return self._curRoom

    def move(self, direction):
        # Move player to next room
        # True if successful, False if not
        next_room = self._curRoom.get_exit(direction)
        if next_room is None:
            return "wall"
        if next_room.is_locked:
            # Return specific status so Engine can ask player for key
            return "locked"

        self._curRoom = next_room
        return "success"

    def pick_up(self, item):
        # Add item to inventory
        self._inventory.append(item)

    def drop(self, item):
        self._inventory.remove(item)

    def has_item(self, itemName):
        return itemName.lower() in [i.lower() for i in self._inventory]
