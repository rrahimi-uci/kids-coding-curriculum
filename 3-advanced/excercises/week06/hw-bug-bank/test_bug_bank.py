"""Checks for Homework 6 - Piggy Bank Bug Hunt."""


def test_deposits_add_up(load_target):
    money = load_target()
    bank = money.PiggyBank("Comet")
    bank.deposit(10)
    bank.deposit(5)
    assert bank.coins == 15, f"Depositing 10 then 5 should give 15 coins, not {bank.coins}."


def test_can_withdraw_everything_but_not_more(load_target):
    money = load_target()
    bank = money.PiggyBank("Comet")
    bank.coins = 15
    assert bank.withdraw(16) is False and bank.coins == 15, "You cannot take 16 coins out of 15."
    assert bank.withdraw(15) is True and bank.coins == 0, "You CAN take all 15 coins out of 15. Check the comparison."


def test_statement_shows_every_line(load_target):
    money = load_target()
    bank = money.PiggyBank("Comet")
    bank.log = ["in 10", "in 5", "out 15"]
    lines = bank.statement()
    assert lines == ["1. in 10", "2. in 5", "3. out 15"], f"The statement should show all 3 log lines. Got {lines}"
