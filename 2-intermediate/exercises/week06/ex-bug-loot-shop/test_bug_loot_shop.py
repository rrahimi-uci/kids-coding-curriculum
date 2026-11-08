"""Checks for Bug Hunt Station 4 - Loot Shop."""


def test_total_adds_every_price(load_target):
    m = load_target()
    answer = m.total_price([12, 5, 30])
    assert answer == 47, f"12 + 5 + 30 = 47, but total_price gave {answer}. Does it stop too early? Check the indent of return."


def test_cheapest(load_target):
    m = load_target()
    answer = m.cheapest([12, 5, 30])
    assert answer == 5, f"The cheapest of [12, 5, 30] is 5, not {answer}. Which variable should be returned?"


def test_can_buy_returns_true_or_false(load_target):
    m = load_target()
    assert m.can_buy(50, [12, 5, 30]) is True, "50 coins is enough for 47: can_buy should RETURN True (not print it)."
    assert m.can_buy(40, [12, 5, 30]) is False, "40 coins is not enough for 47: can_buy should return False."
