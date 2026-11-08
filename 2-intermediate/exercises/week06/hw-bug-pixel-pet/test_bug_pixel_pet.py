"""Checks for Homework 6 - Pixel Pet bug hunt."""

import pytest


def test_play(load_target):
    m = load_target()
    try:
        pet = m.play(m.make_pet("Pixel"))
    except KeyError as error:
        pytest.fail(f"play() crashed with KeyError: {error}. Check the spelling of the key.")
    assert pet["happiness"] == 7 and pet["hunger"] == 6, "After playing: happiness 5 -> 7 and hunger 5 -> 6."


def test_feed_changes_hunger(load_target):
    m = load_target()
    pet = m.feed(m.make_pet("Pixel"))
    assert pet["hunger"] == 2, f"Feeding should take hunger from 5 to 2, but it is {pet['hunger']}."
    assert sorted(pet) == ["happiness", "hunger", "name"], (
        f"The pet should still have only 3 keys, but it has {sorted(pet)}. Keys must match exactly (capital letters!).")


def test_mood_uses_or(load_target):
    m = load_target()
    assert m.mood({"name": "P", "hunger": 9, "happiness": 6}) == "grumpy", "Very hungry (9) should be grumpy."
    assert m.mood({"name": "P", "hunger": 3, "happiness": 1}) == "grumpy", "Very unhappy (1) should be grumpy."
    assert m.mood({"name": "P", "hunger": 3, "happiness": 6}) == "happy", "Not hungry and quite happy: happy."
