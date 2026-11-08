# Inventory Review - YOUR version
# Level 2 warm-up: functions with return, lists, loops and a dictionary.
# A game inventory is a list of item names, e.g. ["gem", "key", "gem"].
# Finish the TODOs, then press Run and see if it does what the README says.


def count_item(items, name):
    """Return how many times name appears in the list."""
    count = 0
    # TODO 1: loop over items and add 1 to count for every match
    return count


def remove_all(items, name):
    """Return a NEW list without any copies of name (the old list is not changed)."""
    kept = []
    # TODO 2: append every item that is NOT name to kept
    return kept


def tally(items):
    """Return a dictionary: item name -> how many. (Already done!)"""
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def most_common(items):
    """Return the item we have most of (the first one found if there is a tie).
    Return None for an empty inventory."""
    best = None
    best_count = 0
    # TODO 3: loop over tally(items).items(). When a count is bigger than
    #         best_count, remember that item and its count.
    return best


if __name__ == "__main__":
    backpack = ["gem", "key", "potion", "gem", "map", "gem", "potion"]
    print("Backpack:", backpack)
    print("Gems:", count_item(backpack, "gem"))
    print("Most common:", most_common(backpack))
    print("After using all potions:", remove_all(backpack, "potion"))
    for item, count in tally(backpack).items():
        print(f"  {count} x {item}")
