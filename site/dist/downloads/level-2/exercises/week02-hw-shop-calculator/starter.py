# Potion Shop Calculator
# Finish the three functions. Each one must RETURN its answer.


def total_cost(price, quantity):
    """Return the cost of buying quantity items that each cost price coins."""
    # TODO 1: return price times quantity.
    pass


def can_afford(coins, cost):
    """Return True if you have enough coins to pay the cost."""
    # TODO 2: return True or False. Tip: coins >= cost
    pass


def coins_left(coins, cost):
    # TODO 3: write a docstring on the line above this one, like the others.
    # TODO 4: if you can afford it, return coins - cost. Otherwise return coins.
    pass


if __name__ == "__main__":
    coins = 50
    price = 12
    print(f"You have {coins} coins. Potions cost {price} coins each.")
    how_many = int(input("How many potions do you want? "))
    cost = total_cost(price, how_many)
    if can_afford(coins, cost):
        print(f"That costs {cost} coins. Here you go!")
    else:
        print(f"That costs {cost} coins. Sorry, you cannot afford it.")
    print(f"Coins left: {coins_left(coins, cost)}")
