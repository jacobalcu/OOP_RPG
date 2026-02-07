# Define Room class
class Room:
    def __init__(self, desc):
        self._desc = desc
        self._exits = {}

    def set_exit(self, direction, neighbor):
        # Connect room to another neighbor in specific dir
        self._exits[direction.lower()] = neighbor

    def get_exit(self, direction):
        # Return room in certain dir, or None if not exist
        return self._exits.get(direction)

    def get_description(self):
        # Return room's description
        return self._desc
