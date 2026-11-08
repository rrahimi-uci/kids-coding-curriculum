"""Checks for Exercise 3.2 - Adventure Inventory."""


def test_add_item_puts_it_at_the_end(load_target):
    m = load_target()
    backpack = m.add_item(["torch"], "rope")
    assert backpack == ["torch", "rope"], f"After adding rope the backpack should be ['torch', 'rope'], not {backpack}."


def test_has_item(load_target):
    m = load_target()
    assert m.has_item(["torch", "map"], "map") is True, "The backpack has a map: has_item should return True."
    assert m.has_item(["torch", "map"], "key") is False, "There is no key: has_item should return False."


def test_last_item_without_crashing(load_target):
    m = load_target()
    try:
        answer = m.last_item(["torch", "rope", "map", "apple"])
    except IndexError:
        raise AssertionError("last_item crashed with IndexError. Four items have index 0 to 3, so the last is len - 1.")
    assert answer == "apple", f"The last item should be 'apple', not {answer!r}."


def test_first_and_last_of_a_one_item_backpack(load_target):
    m = load_target()
    assert m.first_item(["key"]) == "key", "With only a key, the first item is the key."
    assert m.last_item(["key"]) == "key", "With only a key, the last item is the key too."
