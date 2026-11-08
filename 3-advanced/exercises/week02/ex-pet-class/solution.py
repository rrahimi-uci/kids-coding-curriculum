# Pet Class - reference solution
# A class is a blueprint. Every Pet object made from it has its OWN numbers.
# Kind design: our pets never get sick, run away or make you feel guilty.


class Pet:
    """Blueprint for a virtual pet."""

    def __init__(self, name, species):
        # __init__ runs once, when a new pet is made. self is "this pet".
        self.name = name
        self.species = species
        self.hunger = 5      # 0 = full, 10 = very hungry
        self.happiness = 5   # 0 = bored, 10 = very happy

    def feed(self):
        """Feeding makes the pet less hungry (never below 0)."""
        self.hunger = self.hunger - 3
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        """Playing makes the pet happier (max 10) and a little hungrier (max 10)."""
        self.happiness = self.happiness + 2
        if self.happiness > 10:
            self.happiness = 10
        self.hunger = self.hunger + 1
        if self.hunger > 10:
            self.hunger = 10

    def mood(self):
        """Return one word that describes how the pet feels right now."""
        if self.hunger >= 7:
            return "hungry"
        if self.happiness >= 7:
            return "happy"
        if self.happiness <= 3:
            return "bored"
        return "okay"

    def describe(self):
        """Return a sentence about the pet."""
        return f"{self.name} the {self.species} feels {self.mood()}."


if __name__ == "__main__":
    pip = Pet("Pip", "dragon")
    bo = Pet("Bo", "robot cat")
    print(pip.describe())
    print(bo.describe())
    while True:
        choice = input("f = feed Pip, p = play with Pip, q = quit: ").strip().lower()
        if choice == "q":
            print("Bye! Pip and Bo will be fine until next time.")
            break
        if choice == "f":
            pip.feed()
        elif choice == "p":
            pip.play()
        print(pip.describe(), f"(hunger {pip.hunger}, happiness {pip.happiness})")
        print(bo.describe(), "<- Bo did not change: a different object!")
