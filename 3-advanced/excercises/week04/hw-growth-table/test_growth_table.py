"""Checks for Homework 4 - Growth Table."""


def test_linear_worst(load_target):
    growth = load_target()
    assert growth.linear_worst(1000) == 1000, "In the worst case linear search looks at all 1000 items."


def test_halving_steps(load_target):
    growth = load_target()
    expected = {1: 1, 10: 4, 100: 7, 1000: 10, 1000000: 20}
    for n, steps in expected.items():
        got = growth.halving_steps(n)
        assert got == steps, f"Halving {n} until it reaches 0 takes {steps} steps, not {got}."


def test_growth_table_rows(load_target):
    growth = load_target()
    rows = growth.growth_table([10, 100, 1000])
    assert rows == [(10, 10, 4), (100, 100, 7), (1000, 1000, 10)], f"The table rows are not right yet: {rows}"
