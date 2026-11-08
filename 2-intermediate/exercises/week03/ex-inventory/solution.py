# TEACHER REFERENCE SOLUTION: Adventure Inventory (Exercise 3.2)
#
# What the program does: it treats a list as an adventurer's backpack. It adds
# items, shows everything inside, names the first and last item, and checks
# whether a particular item is in the bag.
# Key ideas practiced: list append, index numbers that start at 0, len(), and
# looping with "for item in backpack".
# Approach: each function does one small job on the list. The bug hunt is
# last_item(): a list of 4 items has the index numbers 0, 1, 2 and 3, so the
# last item is at len(backpack) - 1, never at len(backpack).


def add_item(backpack, item):
    """Put an item in the backpack and return the backpack."""
    backpack.append(item)      # append puts the new item at the END of the list
    return backpack


def has_item(backpack, item):
    """Return True if the item is somewhere in the backpack."""
    for thing in backpack:
        if thing == item:
            return True        # found it, so we can stop looking straight away
    return False               # only reached if the loop checked everything and found nothing


def first_item(backpack):
    """Return the item that went in first."""
    return backpack[0]         # counting starts at 0, not 1


def last_item(backpack):
    """Return the item that went in last."""
    # FIX 1: backpack[len(backpack)] looked one box past the end and crashed with
    # IndexError. Counting starts at 0, so the last box is len(backpack) - 1.
    return backpack[len(backpack) - 1]


def show_backpack(backpack):
    """Print every item on its own line, then how many there are."""
    for item in backpack:
        print(f"- {item}")
    print(f"{len(backpack)} items in total.")


if __name__ == "__main__":
    backpack = ["torch", "rope"]
    add_item(backpack, "map")
    add_item(backpack, "apple")
    show_backpack(backpack)
    print(f"First in: {first_item(backpack)}. Last in: {last_item(backpack)}.")
    if has_item(backpack, "map"):
        print("You unfold the map. The treasure is to the north!")
    if not has_item(backpack, "key"):
        print("You still need a key for the chest.")


# Common mistakes children make here:
# - Fixing last_item with a fixed number such as backpack[3]: it works for 4 items
#   but breaks as soon as the bag changes size. Use len(backpack) - 1.
# - Putting "return False" inside the loop (indented too far), so has_item only
#   ever checks the first item.
# - Writing backpack = backpack + item in add_item: adding text to a list is an
#   error. Use backpack.append(item), which changes the list itself.
# - Forgetting that an empty backpack has no first or last item (it would crash).
#
# Another correct way: a negative index counts from the end, and "in" does the
# searching for us.
#   return backpack[-1]          # last_item
#   return item in backpack      # has_item
