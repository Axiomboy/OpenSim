import random

class Person:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 100
        self.food = 2
        self.alive = True

    def act(self, world):
        if not self.alive:
            return f"{self.name} is dead."

        self.hunger += 10
        self.energy -= 5

        if self.hunger >= 100:
            self.alive = False
            return f"{self.name} starved. 💀"

        if self.food > 0 and self.hunger >= 50:
            self.food -= 1
            self.hunger = max(0, self.hunger - 40)
            return f"{self.name} ate food."

        if self.energy < 30:
            self.energy = min(100, self.energy + 40)
            return f"{self.name} rested."

        found = random.randint(0, 3)
        if found > 0:
            self.food += found
            return f"{self.name} gathered {found} food."

        return f"{self.name} wandered around."
