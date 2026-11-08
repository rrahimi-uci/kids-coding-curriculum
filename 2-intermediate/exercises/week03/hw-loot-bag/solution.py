# Loot Bag - reference solution
# random.choice() picks one item from a list. We build a NEW list (the bag)
# by appending one item at a time.

import random

CHEST = ["gold coin", "gold coin", "gold coin", "ruby", "potion", "old boot", "map"]


def open_chest(chest):
    """Return one random item from the chest."""
    return random.choice(chest)


def fill_bag(chest, how_many):
    """Return a new list with how_many random items from the chest."""
    bag = []
    for _ in range(how_many):
        bag.append(open_chest(chest))
    return bag


def count_item(bag, item):
    """Return how many times the item is in the bag."""
    count = 0
    for thing in bag:
        if thing == item:
            count = count + 1
    return count


if __name__ == "__main__":
    bag = fill_bag(CHEST, 6)
    print("You open the chest 6 times and find:")
    for thing in bag:
        print(f"- {thing}")
    print(f"Gold coins: {count_item(bag, 'gold coin')}")
    print(f"Old boots: {count_item(bag, 'old boot')}")
