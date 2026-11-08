# TEACHER REFERENCE SOLUTION: Homework 6 - Piggy Bank Bug Hunt
#
# What the program does: a PiggyBank keeps a coin total for a player and a
# log of every deposit and withdrawal, and can print the log as numbered
# lines. Run prints "Comet has 0 coins" and then the three log lines.
# Key ideas: updating an object's data, comparison operators (> versus >=)
# and off-by-one mistakes in loops.
# Approach: each method does one small job on self.coins or self.log. The
# three bugs were each one small slip in one of those jobs.
#
# The three bugs (marked FIX below):
#   FIX 1: deposit used  self.coins = amount       -> self.coins + amount
#   FIX 2: withdraw used amount >= self.coins      -> amount > self.coins
#   FIX 3: statement used range(len(self.log) - 1) -> range(len(self.log))


class PiggyBank:
    """A savings bank for game coins that keeps a log of every change."""

    def __init__(self, owner_nickname):
        self.owner = owner_nickname
        self.coins = 0
        self.log = []

    def deposit(self, amount):
        """Put coins in. Return False for 0 or negative amounts."""
        if amount <= 0:
            return False  # nothing to put in, so refuse
        # FIX 1: "= amount" threw away the old total each time. We must ADD
        # the new coins to what is already in the bank.
        self.coins = self.coins + amount
        self.log.append(f"in {amount}")
        return True

    def withdraw(self, amount):
        """Take coins out. You can take everything, but never more."""
        # FIX 2: taking exactly all the coins is allowed. Only an amount
        # BIGGER than what we have must be refused, so use ">" not ">=".
        if amount <= 0 or amount > self.coins:
            return False
        self.coins = self.coins - amount
        self.log.append(f"out {amount}")
        return True

    def statement(self):
        """Return numbered log lines, like '1. in 10'."""
        lines = []
        # FIX 3: range(n) already counts 0 up to n - 1, so subtracting 1 more
        # skipped the final log entry.
        for i in range(len(self.log)):
            lines.append(f"{i + 1}. {self.log[i]}")  # +1: people count from 1
        return lines


if __name__ == "__main__":
    bank = PiggyBank("Comet")
    bank.deposit(10)
    bank.deposit(5)
    bank.withdraw(15)
    print(f"{bank.owner} has {bank.coins} coins")
    for line in bank.statement():
        print(line)


# Common mistakes children make here:
#   - Fixing deposit with "+=" in the wrong place, such as before the
#     "amount <= 0" check, so bad amounts still change the total.
#   - Changing withdraw to "amount > self.coins" but forgetting the test
#     for 0 or negative amounts.
#   - Making statement start at 1 with range(1, len(self.log)), which
#     skips the first line instead of the last.
#
# Another correct way for statement(): enumerate numbers the lines for us.
#   return [f"{n}. {entry}" for n, entry in enumerate(self.log, start=1)]
