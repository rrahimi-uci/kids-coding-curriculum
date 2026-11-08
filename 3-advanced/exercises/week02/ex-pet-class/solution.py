"""TEACHER REFERENCE SOLUTION: Pet Class

What the program does: it makes two virtual pets, Pip the dragon and Bo the robot cat. The
child can feed or play with Pip and see that only Pip changes. Each pet describes how it
feels in a short sentence. The pets are kind by design: they never get sick or run away.

Key ideas practiced: a class as a blueprint, self, attributes that belong to one object,
methods that change attributes, keeping numbers inside a range (0 to 10), and f-strings.

Approach: the numbers hunger and happiness live inside each Pet. play changes them and
then "clamps" them with an if so they never pass 10. mood checks the most important
feeling first (hunger), then happiness, and falls back to "okay".
"""


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
        # Step 1: add first, then cut back to the limit if we went over.
        self.happiness = self.happiness + 2
        if self.happiness > 10:
            self.happiness = 10
        # Step 2: playing is tiring, so hunger goes up, with the same upper limit.
        self.hunger = self.hunger + 1
        if self.hunger > 10:
            self.hunger = 10

    def mood(self):
        """Return one word that describes how the pet feels right now."""
        # Step 3: the ORDER matters. A very hungry pet is "hungry" even if it is happy,
        # because the first if that is true ends the method with its return.
        if self.hunger >= 7:
            return "hungry"
        if self.happiness >= 7:
            return "happy"
        if self.happiness <= 3:
            return "bored"
        return "okay"

    def describe(self):
        """Return a sentence about the pet."""
        # Step 4: self.mood() has brackets because it is a method we CALL to get the word.
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


# Common mistakes children make here:
# - Forgetting self. in front of happiness or hunger: Python then says the name is not
#   defined, or changes a throw-away variable instead of the pet.
# - Forgetting the limit: happiness climbs to 12 or 14 because only the "+ 2" was written.
# - Putting the mood checks in the wrong order (for example "okay" first), so the pet is
#   never "hungry" or "happy".
# - Writing self.mood without brackets in describe, which prints a method object.
#
# Another correct way to keep a number at most 10 (min picks the smaller one):
#     self.happiness = min(10, self.happiness + 2)
