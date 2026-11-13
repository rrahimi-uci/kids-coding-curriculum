# Loot Bag
# Open the treasure chest several times and keep what you find in a list.

import random

CHEST = ["gold coin", "gold coin", "gold coin", "ruby", "potion", "old boot", "map"]


def open_chest(chest):
    """Return one random item from the chest."""
    return random.choice(chest)


def fill_bag(chest, how_many):
    """Return a new list with how_many random items from the chest."""
    bag = []
    # TODO 1: repeat how_many times: append open_chest(chest) to the bag.
    return bag


def count_item(bag, item):
    """Return how many times the item is in the bag."""
    count = 0
    # TODO 2: loop over the bag. Each time a thing matches the item, add 1 to count.
    return count


if __name__ == "__main__":
    bag = fill_bag(CHEST, 6)
    print("You open the chest 6 times and find:")
    for thing in bag:
        print(f"- {thing}")
    print(f"Gold coins: {count_item(bag, 'gold coin')}")
    print(f"Old boots: {count_item(bag, 'old boot')}")
