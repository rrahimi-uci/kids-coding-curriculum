"""Checks for Bug Hunt Station 1 - Hero Card."""

import pytest


def card(load_target):
    m = load_target()
    try:
        return m.make_card("Zoe the Brave", 4, 120)
    except TypeError as error:
        pytest.fail(f"make_card crashed with TypeError: {error}. Text + number does not work. Try an f-string.")


def test_card_has_four_lines(load_target):
    lines = card(load_target)
    assert len(lines) == 4, f"The card should have 4 lines, not {len(lines)}."


def test_numbers_appear_on_the_card(load_target):
    lines = card(load_target)
    assert lines[1] == "Level: 4", f"The second line should be 'Level: 4', not {lines[1]!r}."
    assert lines[3] == "Next level: 5", f"The last line should be 'Next level: 5', not {lines[3]!r}."


def test_text_still_works(load_target):
    lines = card(load_target)
    assert lines[0] == "Hero: Zoe the Brave", f"The first line should be 'Hero: Zoe the Brave', not {lines[0]!r}."
