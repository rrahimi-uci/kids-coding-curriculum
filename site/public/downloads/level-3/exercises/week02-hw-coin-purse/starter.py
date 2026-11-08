# Coin Purse - YOUR version
# A CoinPurse object keeps track of the coins a player has in a game.
# The class protects its number: coins can never go below zero.
# Finish the TODOs, then press Run and see if it does what the README says.

SHOP = {"potion": 5, "shield": 12, "map": 3}


class CoinPurse:
    """Blueprint for a purse of game coins."""

    def __init__(self, coins=0):
        self.coins = coins

    def add(self, amount):
        """Add coins. Ignore amounts of 0 or less."""
        # TODO 1: only if amount is more than 0, add it to self.coins
        pass

    def can_afford(self, price):
        """Return True if there are enough coins to pay price."""
        # TODO 2: return True when self.coins is at least price
        return False

    def spend(self, price):
        """Pay price if we can afford it. Return True if paid, False if not."""
        # TODO 3: if self.can_afford(price): take price away and return True
        #         otherwise return False
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
