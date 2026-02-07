# Define Player here
class Player:
    def __init__(self, name, cur_room):
        self._curRoom = cur_room
        self._name = name

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
        if next_room:
            self._curRoom = next_room
            return True
        return False
