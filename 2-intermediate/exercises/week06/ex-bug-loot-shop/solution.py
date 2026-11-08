# TEACHER REFERENCE SOLUTION: Bug Hunt Station 4 - Loot Shop
#
# What it does: works out the total price of a basket, the cheapest item,
# and whether the player has enough coins to buy everything.
# Key ideas: bugs that do NOT crash are the sneakiest - the program runs but
# gives wrong answers. Also: "return" ends a function, and printing a value
# is not the same as giving it back.
# Approach: three small fixes, one per function. We check each one against
# the answers worked out on paper (total 47, cheapest 5, 50 coins is enough).


def total_price(prices):
    """Return all the prices added together."""
    total = 0
    for price in prices:
        total = total + price
    # FIX 1: "return" was indented INSIDE the loop, so the function ended
    # after the first price (it gave 12, not 47). Now it is outside the loop
    # and runs only once every price has been added.
    return total


def cheapest(prices):
    """Return the smallest price."""
    smallest = prices[0]              # start by guessing the first price is smallest
    for price in prices:
        if price < smallest:
            smallest = price          # found a cheaper one: remember it
    # FIX 2: the starter returned prices[0] (always the first item) and threw
    # away the answer the loop had found. We return the variable instead.
    return smallest


def can_buy(coins, prices):
    """Return True if the coins are enough to buy everything."""
    # FIX 3: the starter used print(...), which only shows the answer on the
    # screen and gives back nothing (None), so "if can_buy(...)" was always
    # False. "return" hands the True/False answer back to the caller.
    return coins >= total_price(prices)


if __name__ == "__main__":
    basket = [12, 5, 30]
    print(f"Total: {total_price(basket)} coins")
    print(f"Cheapest item: {cheapest(basket)} coins")
    if can_buy(50, basket):
        print("With 50 coins you can buy everything!")
    else:
        print("With 50 coins you cannot buy everything.")


# Common mistakes children make here:
# - Fixing total_price by deleting the "return" altogether, so the function
#   gives back nothing. The return must stay, just not inside the loop.
# - Fixing cheapest by changing prices[0] to prices[1], which only happens
#   to work for this basket. It must return the variable "smallest".
# - Keeping the print() in can_buy and adding "return" below it, or writing
#   "return print(...)". The function should just return the comparison.
#
# Another correct way: Python already has helpers for the first two jobs:
#     total_price: return sum(prices)
#     cheapest:    return min(prices)
