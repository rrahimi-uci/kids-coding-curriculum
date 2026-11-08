# Adventure Inventory - reference solution
# The backpack is a list. Index 0 is the FIRST item, and the last item is
# at index len(backpack) - 1 (or simply -1).


def add_item(backpack, item):
    """Put an item in the backpack and return the backpack."""
    backpack.append(item)
    return backpack


def has_item(backpack, item):
    """Return True if the item is somewhere in the backpack."""
    for thing in backpack:
        if thing == item:
            return True
    return False


def first_item(backpack):
    """Return the item that went in first."""
    return backpack[0]


def last_item(backpack):
    """Return the item that went in last."""
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
