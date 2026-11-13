"""Checks for Homework 2 - Potion Shop Calculator."""


def test_total_cost(load_target):
    m = load_target()
    answer = m.total_cost(12, 3)
    assert answer == 36, f"3 potions at 12 coins each cost 36 coins, but total_cost(12, 3) returned {answer}."


def test_can_afford(load_target):
    m = load_target()
    assert m.can_afford(50, 36) is True, "With 50 coins you CAN afford 36. Return True."
    assert m.can_afford(50, 50) is True, "With 50 coins you CAN afford exactly 50."
    assert m.can_afford(50, 60) is False, "With 50 coins you can NOT afford 60. Return False."


def test_coins_left(load_target):
    m = load_target()
    assert m.coins_left(50, 36) == 14, "50 coins minus 36 leaves 14."
    assert m.coins_left(50, 60) == 50, "If you cannot afford it, you keep all 50 coins."


def test_coins_left_has_a_docstring(load_target):
    m = load_target()
    doc = m.coins_left.__doc__
    assert doc and len(doc.strip()) > 10, 'Give coins_left a docstring: """Return ...""" under the def line (TODO 3).'
