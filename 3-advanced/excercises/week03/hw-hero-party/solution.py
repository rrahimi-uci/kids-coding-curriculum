# Hero Party - reference solution
# Inheritance: Healer, Builder and Explorer are all Heroes.
# Composition: a Party HAS a list of heroes.


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
        super().__init__(name, "building")

    def action(self):
        return f"{self.name} builds a bridge."


class Explorer(Hero):
    def __init__(self, name):
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
