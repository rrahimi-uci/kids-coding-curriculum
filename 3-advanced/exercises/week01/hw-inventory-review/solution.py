"""TEACHER REFERENCE SOLUTION: Inventory Review

What the program does: it treats a game backpack as a list of item names (like
["gem", "key", "gem"]) and answers questions about it: how many of one item, what is the most
common item, and what is left after removing every copy of an item.

Key ideas practiced: functions that return, lists, for loops, if checks, a counter
variable, and a dictionary that maps a name to a count.

Approach: count_item and remove_all are one loop each. most_common reuses the finished
tally dictionary and keeps the "best so far", the same pattern as finding the highest score.
"""


def count_item(items, name):
    """Return how many times name appears in the list."""
    count = 0  # start at zero, because we have not seen any yet
    for item in items:
        if item == name:
            count += 1
    return count


def remove_all(items, name):
    """Return a NEW list without any copies of name (the old list is not changed)."""
    # Building a new list (instead of deleting from items while looping over it) keeps the
    # caller's backpack safe and avoids a classic bug where items get skipped.
    kept = []
    for item in items:
        if item != name:
            kept.append(item)
    return kept


def tally(items):
    """Return a dictionary: item name -> how many."""
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1  # first time we see this item
    return counts


def most_common(items):
    """Return the item we have most of (the first one found if there is a tie).
    Return None for an empty inventory."""
    best = None
    best_count = 0
    for item, count in tally(items).items():
        # Strictly bigger (>), not ">=": on a tie the first item found keeps the crown.
        # An empty backpack never enters the loop, so best stays None.
        if count > best_count:
            best = item
            best_count = count
    return best


if __name__ == "__main__":
    backpack = ["gem", "key", "potion", "gem", "map", "gem", "potion"]
    print("Backpack:", backpack)
    print("Gems:", count_item(backpack, "gem"))
    print("Most common:", most_common(backpack))
    print("After using all potions:", remove_all(backpack, "potion"))
    for item, count in tally(backpack).items():
        print(f"  {count} x {item}")


# Common mistakes children make here:
# - Using items.remove(name) or del inside the loop: it changes the original list (a
#   test checks this) and can skip items. Build a new list instead.
# - Starting count = 1 or putting return count inside the loop, so the answer is wrong
#   after the first item.
# - In most_common, setting best_count to the wrong starting value, or using >= so the
#   LAST tied item wins, or forgetting to return None for an empty backpack.
#
# Another correct way for count_item (lists can count for you):
#     return items.count(name)
