"""TEACHER REFERENCE SOLUTION: Hero Party

What the program does: it builds a party of heroes (a Healer, a Builder, an Explorer and a
plain Hero). When the party takes a turn, every hero says what it does, and the sentences
are collected in a list and printed.

Key ideas practiced: inheritance (each hero type is a Hero), `super().__init__` to set the
parent's attributes, overriding `action()`, and composition (a Party HAS a list of heroes).

Approach: Builder and Explorer copy the pattern of the finished Healer: pass their own power
word to the parent and replace `action()`. `Party.take_turn` simply asks each hero for its
action; it never checks which type a hero is, because each hero already knows what to say.
"""


class Hero:
    """Parent class for every hero."""

    def __init__(self, name, power="courage"):
        self.name = name
        self.power = power

    def action(self):
        return f"{self.name} cheers the team on."


class Healer(Hero):
    def __init__(self, name):
        super().__init__(name, "healing")

    def action(self):
        return f"{self.name} heals the team."


class Builder(Hero):
    def __init__(self, name):
        # Step 1: the parent stores name and power. We choose the power: "building".
        super().__init__(name, "building")

    def action(self):
        # Step 2: overriding means this version replaces Hero.action for Builders.
        return f"{self.name} builds a bridge."


class Explorer(Hero):
    def __init__(self, name):
        # Step 3: same pattern as Healer and Builder, with the power "exploring".
        super().__init__(name, "exploring")

    def action(self):
        return f"{self.name} maps the cave."


class Party:
    """A group of heroes. The Party HAS heroes (composition)."""

    def __init__(self):
        self.heroes = []

    def add(self, hero):
        self.heroes.append(hero)

    def take_turn(self):
        """Every hero acts once. Return the list of action sentences."""
        actions = []
        # Step 4: the same call, hero.action(), gives a different sentence for each class.
        for hero in self.heroes:
            actions.append(hero.action())
        return actions


if __name__ == "__main__":
    party = Party()
    party.add(Healer("Amara"))
    party.add(Builder("Kenji"))
    party.add(Explorer("Sofia"))
    party.add(Hero("Ravi"))
    for sentence in party.take_turn():
        print(sentence)


# Common mistakes children make here:
# - Forgetting `super().__init__(name, "building")`, so `name` and `power` are never set.
# - Writing `class Builder:` without `(Hero)`, so Builder is not a Hero.
# - Returning from inside the loop in take_turn (only the first hero acts), or using `print`
#   instead of `return`.
# - Forgetting the brackets in `hero.action()`, which stores the method, not the sentence.
#
# Another correct way for take_turn (a list comprehension):
#     return [hero.action() for hero in self.heroes]
