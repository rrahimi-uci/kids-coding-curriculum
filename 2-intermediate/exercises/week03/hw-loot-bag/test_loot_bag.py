"""Checks for Homework 3 - Loot Bag."""

import random


def test_bag_has_the_right_number_of_items(load_target):
    m = load_target()
    random.seed(3)
    bag = m.fill_bag(m.CHEST, 5)
    assert len(bag) == 5, f"fill_bag(CHEST, 5) should give back 5 items, but the bag has {len(bag)}."


def test_everything_in_the_bag_came_from_the_chest(load_target):
    m = load_target()
    random.seed(7)
    bag = m.fill_bag(["ruby", "map"], 10)
    assert bag and all(thing in ["ruby", "map"] for thing in bag), "Every item in the bag must come from the chest."


def test_count_item(load_target):
    m = load_target()
    bag = ["ruby", "map", "ruby", "potion", "ruby"]
    assert m.count_item(bag, "ruby") == 3, "There are 3 rubies in ['ruby', 'map', 'ruby', 'potion', 'ruby']."
    assert m.count_item(bag, "old boot") == 0, "There are no old boots, so the count is 0."
