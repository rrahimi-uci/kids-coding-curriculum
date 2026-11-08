"""Checks for Exercise 5.1 - Sort Race."""

import random

CARDS = [7, 3, 9, 1, 5, 3, 8, 2]


def test_bubble_sort_sorts_and_keeps_every_item(load_target):
    sorts = load_target()
    result, _ = sorts.bubble_sort(CARDS)
    assert result == sorted(CARDS), f"bubble_sort should give {sorted(CARDS)}, not {result}. (Both 3s must stay!)"


def test_original_list_is_not_changed(load_target):
    sorts = load_target()
    cards = list(CARDS)
    sorts.bubble_sort(cards)
    sorts.selection_sort(cards)
    assert cards == CARDS, "Sorting should make a NEW list and leave the original cards alone."


def test_bubble_sort_counts_swaps(load_target):
    sorts = load_target()
    _, swaps = sorts.bubble_sort([3, 2, 1])
    assert swaps == 3, f"Bubble sort needs 3 swaps for [3, 2, 1] (3-2, 3-1, 2-1), not {swaps}."
    _, swaps = sorts.bubble_sort([1, 2, 3])
    assert swaps == 0, "An already sorted list needs 0 swaps."


def test_both_sorts_agree_on_random_lists(load_target):
    sorts = load_target()
    rng = random.Random(5)
    for _ in range(20):
        items = [rng.randint(0, 20) for _ in range(rng.randint(0, 12))]
        assert sorts.bubble_sort(items)[0] == sorted(items), f"bubble_sort got {items} wrong."
        result, swaps = sorts.selection_sort(items)
        assert result == sorted(items) and swaps <= max(len(items) - 1, 0), "selection_sort should sort with at most n - 1 swaps."
