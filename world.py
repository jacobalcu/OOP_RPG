# Define Room class
opposite_directions = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
}


class Room:
    def __init__(self, desc, is_locked=False, lock_id=None):
        self._desc = desc
        self._exits = {}
        self._items = []

        self.is_locked = is_locked
        self.lock_id = lock_id

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item_name):
        """Find item by name, remove, and return object"""
        for item in self._items:
            if item.name.lower() == item_name.lower():
                self._items.remove(item)
                return item
        return None

    def set_exit(self, direction, neighbor):
        # Connect room to another neighbor in specific dir
        # Create bidirectional connection to clean up Game class
        self._exits[direction.lower()] = neighbor
        neighbor._exits[opposite_directions[direction.lower()]] = self

    def get_exit(self, direction):
        # Return room in certain dir, or None if not exist
        return self._exits.get(direction.lower())

    def get_description(self):
        # Return room's description
        display_text = f"You are in {self._desc}"

        item_list = ", ".join([i.name for i in self._items])
        if item_list:
            display_text += f"\nItems in this room: {item_list}"

        exit_names = ", ".join(self._exits.keys())
        display_text += f"\nExits: {exit_names}"

        return display_text
