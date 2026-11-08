# Bug Hunt Station 4: Loot Shop - FIXED version (teacher)
# Bug 1: total_price() had "return" INSIDE the loop, so it stopped after
#        the first price. Fix: un-indent return so it runs after the loop.
# Bug 2: cheapest() returned prices[0] instead of the variable it worked out.
# Bug 3: can_buy() printed the answer instead of returning it.


def total_price(prices):
    """Return all the prices added together."""
    total = 0
    for price in prices:
        total = total + price
    return total


def cheapest(prices):
    """Return the smallest price."""
    smallest = prices[0]
    for price in prices:
        if price < smallest:
            smallest = price
    return smallest


def can_buy(coins, prices):
    """Return True if the coins are enough to buy everything."""
    return coins >= total_price(prices)


if __name__ == "__main__":
    basket = [12, 5, 30]
    print(f"Total: {total_price(basket)} coins")
    print(f"Cheapest item: {cheapest(basket)} coins")
    if can_buy(50, basket):
        print("With 50 coins you can buy everything!")
    else:
        print("With 50 coins you cannot buy everything.")
