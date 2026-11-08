"""Checks for Homework 3 - Hero Party."""


def test_builder_and_explorer_are_heroes_with_powers(load_target):
    heroes = load_target()
    kenji, sofia = heroes.Builder("Kenji"), heroes.Explorer("Sofia")
    assert isinstance(kenji, heroes.Hero) and isinstance(sofia, heroes.Hero), "Builder and Explorer should inherit from Hero."
    assert (kenji.power, sofia.power) == ("building", "exploring"), (
        "Use super().__init__(name, 'building') and super().__init__(name, 'exploring')."
    )


def test_each_hero_acts_differently(load_target):
    heroes = load_target()
    assert heroes.Builder("Kenji").action() == "Kenji builds a bridge.", "Builder.action() should say '<name> builds a bridge.'"
    assert heroes.Explorer("Sofia").action() == "Sofia maps the cave.", "Explorer.action() should say '<name> maps the cave.'"


def test_party_take_turn(load_target):
    heroes = load_target()
    party = heroes.Party()
    party.add(heroes.Healer("Amara"))
    party.add(heroes.Hero("Ravi"))
    actions = party.take_turn()
    assert actions == ["Amara heals the team.", "Ravi cheers the team on."], (
        f"take_turn should return one sentence per hero, in order. Got {actions!r}"
    )
