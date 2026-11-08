"""Checks for Homework 1 - Dragon Door."""


def test_key_and_level_three_opens(load_target):
    m = load_target()
    assert m.door_opens(True, 5) is True, "Key + level 5 should open the door."
    assert m.door_opens(True, 3) is True, "Key + level 3 should open the door (3 or more)."


def test_key_but_level_too_low_stays_shut(load_target):
    m = load_target()
    assert m.door_opens(True, 2) is False, "Key but only level 2: the door should stay shut. Use 'and'."


def test_legends_do_not_need_a_key(load_target):
    m = load_target()
    assert m.door_opens(False, 10) is True, "Level 10 with NO key should still open the door. Use 'or'."
    assert m.door_opens(False, 4) is False, "No key and level 4: the door should stay shut."


def test_message_says_hero_name(run_target):
    out = run_target(inputs=["Sky Fox", "yes", "5"]).stdout
    assert "Sky Fox" in out, "The message should say the hero's name. Use an f-string (TODO 2)."
