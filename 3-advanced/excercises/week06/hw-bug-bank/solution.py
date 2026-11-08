# Homework 6: Piggy Bank Bug Hunt - FIXED version (teacher)
# The three bugs:
#   1. deposit used  self.coins = amount   -> self.coins = self.coins + amount
#   2. withdraw used amount >= self.coins  -> amount > self.coins (you CAN take all)
#   3. statement used range(len(self.log) - 1) -> range(len(self.log)) (last line lost)


class PiggyBank:
    """A savings bank for game coins that keeps a log of every change."""

    def __init__(self, owner_nickname):
        self.owner = owner_nickname
        self.coins = 0
        self.log = []

    def deposit(self, amount):
        """Put coins in. Return False for 0 or negative amounts."""
        if amount <= 0:
            return False
        self.coins = self.coins + amount
        self.log.append(f"in {amount}")
        return True

    def withdraw(self, amount):
        """Take coins out. You can take everything, but never more."""
        if amount <= 0 or amount > self.coins:
            return False
        self.coins = self.coins - amount
        self.log.append(f"out {amount}")
        return True

    def statement(self):
        """Return numbered log lines, like '1. in 10'."""
        lines = []
        for i in range(len(self.log)):
            lines.append(f"{i + 1}. {self.log[i]}")
        return lines


if __name__ == "__main__":
    bank = PiggyBank("Comet")
    bank.deposit(10)
    bank.deposit(5)
    bank.withdraw(15)
    print(f"{bank.owner} has {bank.coins} coins")
    for line in bank.statement():
        print(line)
