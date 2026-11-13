# TEACHER REFERENCE SOLUTION: Loot Bag (Homework 3)
#
# What the program does: it opens a treasure chest 6 times, keeps every random
# find in a bag (a list), then counts the gold coins and old boots in the bag.
# Key ideas practiced: building a NEW list with append() inside a loop, and
# counting things with a loop and a counter variable.
# Approach: fill_bag() starts with an empty list and adds one random item for each
# time we open the chest. count_item() starts a counter at 0 and adds 1 each time
# it sees the item we are looking for. The chest lists "gold coin" three times, so
# coins are three times as likely to be picked as the ruby.

import random

CHEST = ["gold coin", "gold coin", "gold coin", "ruby", "potion", "old boot", "map"]


def open_chest(chest):
    """Return one random item from the chest."""
    return random.choice(chest)     # every position in the list is equally likely


def fill_bag(chest, how_many):
    """Return a new list with how_many random items from the chest."""
    bag = []                        # start empty, then fill it up
    for _ in range(how_many):       # _ means we do not need the loop counter
        bag.append(open_chest(chest))
    return bag


def count_item(bag, item):
    """Return how many times the item is in the bag."""
    count = 0                       # start at zero and add one for every match
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


# Common mistakes children make here:
# - Putting "bag = []" inside the loop, so the bag is emptied every time and
#   ends up with only one item.
# - Putting "return bag" or "return count" inside the loop (indented too far), so
#   the function ends after the first pass.
# - Writing count = 1 instead of count = count + 1, or putting the +1 outside the
#   if, which counts every item rather than only the matching ones.
# - Writing bag + open_chest(chest) instead of bag.append(...): the bag is not changed.
#
# Another correct way: the list method count() does the counting for us.
#   return bag.count(item)
