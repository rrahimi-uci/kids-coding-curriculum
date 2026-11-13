# TEACHER REFERENCE SOLUTION: Potion Shop Calculator (Homework 2)
#
# What the program does: the shop sells potions for 12 coins each and the hero
# has 50 coins. It asks how many potions to buy, shows the cost, says whether the
# hero can afford them and how many coins are left.
# Key ideas practiced: functions that return answers, a True/False function, a
# function that calls another function, and docstrings (a note in triple quotes
# that says what a function does).
# Approach: three tiny functions, each doing one job. coins_left() reuses
# can_afford(), so the "enough coins?" rule is written only once.


def total_cost(price, quantity):
    """Return the cost of buying quantity items that each cost price coins."""
    return price * quantity


def can_afford(coins, cost):
    """Return True if you have enough coins to pay the cost."""
    # ">=" and not ">" because paying exactly all your coins is allowed.
    return coins >= cost


def coins_left(coins, cost):
    """Return the coins left after paying. If you cannot afford it, you keep all your coins."""
    if can_afford(coins, cost):        # a function can call another function
        return coins - cost
    return coins                       # no purchase happens, so nothing is spent


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


# Common mistakes children make here:
# - Leaving pass in the function after adding code, or printing instead of
#   returning, so the caller gets None.
# - Using "coins > cost" in can_afford: then spending exactly 50 of 50 coins is
#   wrongly refused (the tests check this case).
# - Putting the docstring below the first line of code; it must be the very first
#   thing under the def line, or Python does not treat it as a docstring.
# - Always returning coins - cost, so the coins go negative when the hero cannot pay.
#
# Another correct way: the same function without calling can_afford().
#   if coins >= cost:
#       return coins - cost
#   return coins
