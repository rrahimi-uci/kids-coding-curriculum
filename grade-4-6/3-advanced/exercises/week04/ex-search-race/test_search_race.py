"""Checks for Exercise 4.1 - Search Race."""

EVENS = list(range(0, 100, 2))  # 0, 2, 4, ... 98 (sorted, 50 items)


def test_linear_search_counts_steps(load_target):
    search = load_target()
    assert search.linear_search([7, 3, 9], 7) == (0, 1), "Finding the first item takes 1 step."
    assert search.linear_search([7, 3, 9], 9) == (2, 3), "Finding the third item takes 3 steps."
    assert search.linear_search([7, 3, 9], 5) == (-1, 3), "A missing item: index -1 after checking all 3."


def test_binary_search_finds_every_item(load_target):
    search = load_target()
    for index, value in enumerate(EVENS):
        found, _ = search.binary_search(EVENS, value)
        assert found == index, f"binary_search should find {value} at index {index}, but returned {found}."


def test_binary_search_missing_items(load_target):
    search = load_target()
    for value in [-1, 1, 51, 99, 100]:
        found, _ = search.binary_search(EVENS, value)
        assert found == -1, f"{value} is not in the list, so binary_search should return -1, not {found}."


def test_binary_search_is_fast(load_target):
    search = load_target()
    items = list(range(1000))
    worst = max(search.binary_search(items, value)[1] for value in items)
    assert 1 <= worst <= 10, f"Binary search on 1000 items should never need more than 10 steps. Yours needed {worst}."
