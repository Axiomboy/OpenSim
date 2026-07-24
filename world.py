from person import Person


class World:
    def __init__(self):
        names = [
            "Alex", "Sam", "Jordan", "Taylor", "Morgan",
            "Casey", "Jamie", "Riley", "Avery", "Cameron"
        ]

        self.people = [Person(name) for name in names]
        self.day = 0

    def run_day(self):
        self.day += 1

        print(f"\n--- DAY {self.day} ---")

        for person in self.people:
            print(person.act(self))

        alive = [person for person in self.people if person.alive]

        print(f"\nPopulation: {len(alive)}")
        print(f"Deaths: {len(self.people) - len(alive)}")

        return len(alive)
