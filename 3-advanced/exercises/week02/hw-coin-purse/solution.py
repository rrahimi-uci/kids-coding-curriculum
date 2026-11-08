# Coin Purse - reference solution
# A CoinPurse object keeps track of the coins a player has in a game.
# The class protects its number: coins can never go below zero.

SHOP = {"potion": 5, "shield": 12, "map": 3}


class CoinPurse:
    """Blueprint for a purse of game coins."""

    def __init__(self, coins=0):
        self.coins = coins

    def add(self, amount):
        """Add coins. Ignore amounts of 0 or less."""
        if amount > 0:
            self.coins = self.coins + amount

    def can_afford(self, price):
        """Return True if there are enough coins to pay price."""
        return self.coins >= price

    def spend(self, price):
        """Pay price if we can afford it. Return True if paid, False if not."""
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
