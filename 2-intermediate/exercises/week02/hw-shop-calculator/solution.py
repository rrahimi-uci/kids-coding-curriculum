# Potion Shop Calculator - reference solution
# Small functions that return answers. Each one has a docstring: a note in
# triple quotes that says what the function does.


def total_cost(price, quantity):
    """Return the cost of buying quantity items that each cost price coins."""
    return price * quantity


def can_afford(coins, cost):
    """Return True if you have enough coins to pay the cost."""
    return coins >= cost


def coins_left(coins, cost):
    """Return the coins left after paying. If you cannot afford it, you keep all your coins."""
    if can_afford(coins, cost):
        return coins - cost
    return coins


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
