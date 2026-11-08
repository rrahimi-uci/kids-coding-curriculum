"""Checks for Homework 2 - Coin Purse."""


def test_add_coins(load_target):
    game = load_target()
    purse = game.CoinPurse(10)
    purse.add(5)
    assert purse.coins == 15, f"10 coins + 5 should be 15, not {purse.coins}."
    purse.add(-3)
    purse.add(0)
    assert purse.coins == 15, "Adding 0 or a negative amount should not change the purse."


def test_can_afford(load_target):
    game = load_target()
    purse = game.CoinPurse(10)
    assert purse.can_afford(10), "With 10 coins you CAN afford something that costs exactly 10."
    assert not purse.can_afford(11), "With 10 coins you can NOT afford something that costs 11."


def test_spend_never_goes_below_zero(load_target):
    game = load_target()
    purse = game.CoinPurse(10)
    assert purse.spend(4) is True and purse.coins == 6, "spend(4) from 10 should return True and leave 6."
    assert purse.spend(7) is False and purse.coins == 6, "spend(7) with only 6 should return False and keep 6."
