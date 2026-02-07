# Define Room class
opposite_directions = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
}


class Room:
    def __init__(self, desc):
        self._desc = desc
        self._exits = {}
        self.is_locked = False

    def set_exit(self, direction, neighbor):
        # Connect room to another neighbor in specific dir
        # Create bidirectional connection to clean up Game class
        self._exits[direction.lower()] = neighbor
        neighbor._exits[opposite_directions[direction.lower()]] = self

    def get_exit(self, direction):
        # Return room in certain dir, or None if not exist
        return self._exits.get(direction)

    def get_description(self):
        # Return room's description
        return self._desc
