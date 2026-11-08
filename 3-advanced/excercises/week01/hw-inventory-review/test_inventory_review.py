"""Checks for Homework 1 - Inventory Review."""

BACKPACK = ["gem", "key", "potion", "gem", "map", "gem", "potion"]


def test_count_item(load_target):
    inv = load_target()
    assert inv.count_item(BACKPACK, "gem") == 3, "There are 3 gems in the backpack."
    assert inv.count_item(BACKPACK, "sword") == 0, "There are no swords, so the answer should be 0."


def test_remove_all_makes_a_new_list(load_target):
    inv = load_target()
    backpack = list(BACKPACK)
    result = inv.remove_all(backpack, "potion")
    assert result == ["gem", "key", "gem", "map", "gem"], f"Without potions the list should be gems, key and map. Got {result!r}"
    assert backpack == BACKPACK, "remove_all should not change the original list - build a new one."


def test_most_common(load_target):
    inv = load_target()
    assert inv.most_common(BACKPACK) == "gem", "Gem appears 3 times, more than anything else."
    assert inv.most_common([]) is None, "An empty backpack has no most common item: return None."
