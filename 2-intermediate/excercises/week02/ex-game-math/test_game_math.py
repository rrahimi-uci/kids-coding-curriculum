"""Checks for Exercise 2.1 - Game Math."""


def test_xp_needed_returns_a_number(load_target):
    m = load_target()
    answer = m.xp_needed(5)
    assert answer is not None, "xp_needed(5) gave back None. Did it print instead of return? (TODO 1)"
    assert answer == 500, f"Level 5 needs 5 * 100 = 500 XP, but xp_needed(5) returned {answer}."
    assert m.xp_needed(1) == 100, "Level 1 needs 100 XP."


def test_damage_after_shield(load_target):
    m = load_target()
    answer = m.damage(12, 5)
    assert answer is not None, "damage(12, 5) gave back None. Add a return line. (TODO 3)"
    assert answer == 7, f"An attack of 12 against a shield of 5 should do 7 damage, not {answer}."


def test_damage_is_never_negative(load_target):
    m = load_target()
    answer = m.damage(3, 5)
    assert answer == 0, f"An attack of 3 against a shield of 5 should do 0 damage, not {answer}. (TODO 2)"


def test_critical_hits(load_target):
    m = load_target()
    assert m.is_critical(20) is True, "A roll of 20 is a critical hit: return True."
    assert m.is_critical(19) is True, "A roll of 19 is a critical hit too."
    assert m.is_critical(7) is False, "A roll of 7 is not a critical hit: return False."
