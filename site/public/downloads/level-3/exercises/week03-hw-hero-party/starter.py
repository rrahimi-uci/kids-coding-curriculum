# Hero Party - YOUR version
# Inheritance: Healer, Builder and Explorer are all Heroes.
# Composition: a Party HAS a list of heroes.
# Finish the TODOs, then press Run and see if it does what the README says.


class Hero:
    """Parent class for every hero."""

    def __init__(self, name, power="courage"):
        self.name = name
        self.power = power

    def action(self):
        return f"{self.name} cheers the team on."


class Healer(Hero):
    """(Already done - copy this pattern!)"""

    def __init__(self, name):
        super().__init__(name, "healing")

    def action(self):
        return f"{self.name} heals the team."


class Builder(Hero):
    # TODO 1: __init__(self, name) that calls super().__init__(name, "building")
    # TODO 2: action(self) that returns f"{self.name} builds a bridge."
    pass


class Explorer(Hero):
    # TODO 3: __init__ with power "exploring", and action() that returns
    #         f"{self.name} maps the cave."
    pass


class Party:
    """A group of heroes. The Party HAS heroes (composition)."""

    def __init__(self):
        self.heroes = []

    def add(self, hero):
        self.heroes.append(hero)

    def take_turn(self):
        """Every hero acts once. Return the list of action sentences."""
        actions = []
        # TODO 4: loop over self.heroes and append hero.action() to actions
        return actions


if __name__ == "__main__":
    party = Party()
    party.add(Healer("Amara"))
    party.add(Builder("Kenji"))
    party.add(Explorer("Sofia"))
    party.add(Hero("Ravi"))
    for sentence in party.take_turn():
        print(sentence)
