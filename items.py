class Item:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    @property
    def name(self):
        return self._name

    def __str__(self):
        # Magic method that lets you print object directly
        return f"{self._name}: {self._description}"


class Key(Item):
    def __init__(self, name, description, lock_id):
        super().__init__(name, description)
        self.lock_id = lock_id


class Potion(Item):
    def __init__(self, name, description, heal_amount):
        super().__init__(name, description)
        self.heal_amount = heal_amount

    def use(self, target):
        # Behavior unique to Potions
        target.heal(self.heal_amount)
        print(f"You used {self.name} and healed for {self.heal_amount}!")
