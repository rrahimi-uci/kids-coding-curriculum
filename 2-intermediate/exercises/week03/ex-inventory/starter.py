# Adventure Inventory
# The backpack is a list. Press Run: there is an IndexError to hunt down!


def add_item(backpack, item):
    """Put an item in the backpack and return the backpack."""
    # TODO 1: append the item to the backpack.
    return backpack


def has_item(backpack, item):
    """Return True if the item is somewhere in the backpack."""
    # TODO 2: loop over the backpack. If a thing matches the item, return True.
    # After the loop, return False.
    return False


def first_item(backpack):
    """Return the item that went in first."""
    return backpack[0]


def last_item(backpack):
    """Return the item that went in last."""
    # TODO 3 (bug hunt): this line crashes with IndexError. Why?
    # Hint: a list of 4 items has the index numbers 0, 1, 2 and 3.
    return backpack[len(backpack)]


def show_backpack(backpack):
    """Print every item on its own line, then how many there are."""
    for item in backpack:
        print(f"- {item}")
    print(f"{len(backpack)} items in total.")


if __name__ == "__main__":
    backpack = ["lantern", "rope"]
    add_item(backpack, "map")
    add_item(backpack, "apple")
    show_backpack(backpack)
    print(f"First in: {first_item(backpack)}. Last in: {last_item(backpack)}.")
    if has_item(backpack, "map"):
        print("You unfold the map. The treasure is to the north!")
    if not has_item(backpack, "key"):
        print("You still need a key for the chest.")
