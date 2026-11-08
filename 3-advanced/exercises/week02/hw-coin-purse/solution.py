"""TEACHER REFERENCE SOLUTION: Coin Purse

What the program does: it models a player's purse of game coins. The player can add coins
and spend coins in a small shop, but the purse refuses to spend more than it has, so the
number of coins can never go below zero.

Key ideas practiced: a class that "protects" its own data, `if` checks inside methods, a
method that calls another method, and returning True or False to report success.

Approach: `can_afford` answers the yes/no question. `spend` asks `can_afford` first and only
then changes `self.coins`, so the check and the payment can never disagree.
"""

SHOP = {"potion": 5, "shield": 12, "map": 3}


class CoinPurse:
    """Blueprint for a purse of game coins."""

    def __init__(self, coins=0):
        # coins=0 is a default: CoinPurse() starts empty, CoinPurse(10) starts with 10.
        self.coins = coins

    def add(self, amount):
        """Add coins. Ignore amounts of 0 or less."""
        # Step 1: a negative "add" would secretly take coins away, so we ignore it.
        if amount > 0:
            self.coins = self.coins + amount

    def can_afford(self, price):
        """Return True if there are enough coins to pay price."""
        # Step 2: ">=" (not ">") because exactly enough coins is still enough.
        return self.coins >= price

    def spend(self, price):
        """Pay price if we can afford it. Return True if paid, False if not."""
        # Step 3: reuse can_afford instead of repeating the comparison.
        if self.can_afford(price):
            self.coins = self.coins - price
            return True
        return False

    def describe(self):
        return f"{self.coins} coins"


if __name__ == "__main__":
    purse = CoinPurse(10)
    print("You have", purse.describe())
    for item, price in SHOP.items():
        if purse.spend(price):
            print(f"Bought a {item} for {price}. Left: {purse.describe()}")
        else:
            print(f"Not enough coins for a {item} ({price}).")
    purse.add(7)
    print("Found 7 coins! Now:", purse.describe())


# Common mistakes children make here:
# - Using `>` in can_afford, so a purse with exactly 10 coins cannot buy a price-10 item.
# - Taking the coins away BEFORE checking, so the purse can go below zero.
# - Forgetting `return True` after paying, so spend returns None (the test wants True).
# - Writing `self.coins + amount` without `self.coins =` in front, so nothing changes.
#
# Another correct way for spend (check first, leave early):
#     if price > self.coins:
#         return False
#     self.coins -= price
#     return True
