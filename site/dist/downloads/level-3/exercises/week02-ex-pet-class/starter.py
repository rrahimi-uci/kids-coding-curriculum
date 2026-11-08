# Pet Class - YOUR version
# A class is a blueprint. Every Pet object made from it has its OWN numbers.
# Kind design: our pets never get sick, run away or make you feel guilty.
# Finish the TODOs, then press Run and see if it does what the README says.


class Pet:
    """Blueprint for a virtual pet."""

    def __init__(self, name, species):
        # __init__ runs once, when a new pet is made. self is "this pet".
        self.name = name
        self.species = species
        self.hunger = 5      # 0 = full, 10 = very hungry
        self.happiness = 5   # 0 = bored, 10 = very happy

    def feed(self):
        """Feeding makes the pet less hungry (never below 0). (Already done!)"""
        self.hunger = self.hunger - 3
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        """Playing makes the pet happier (max 10) and a little hungrier (max 10)."""
        # TODO 1: add 2 to self.happiness, but never go above 10
        # TODO 2: add 1 to self.hunger, but never go above 10
        pass

    def mood(self):
        """Return one word that describes how the pet feels right now."""
        # TODO 3: return "hungry" if hunger is 7 or more,
        #         otherwise "happy" if happiness is 7 or more,
        #         otherwise "bored" if happiness is 3 or less,
        #         otherwise "okay"
        return "okay"

    def describe(self):
        """Return a sentence about the pet, like 'Pip the dragon feels okay.'"""
        # TODO 4: use an f-string with self.name, self.species and self.mood()
        return ""


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
