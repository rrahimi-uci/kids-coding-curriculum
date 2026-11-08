# Bug Hunt Station 4: Loot Shop
# No red errors here - but the answers are WRONG. These are the sneakiest bugs!
# There are THREE bugs, one in each function. Work out the right answers on
# paper first, then use print() to see where the program goes wrong.


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
    return prices[0]


def can_buy(coins, prices):
    """Return True if the coins are enough to buy everything."""
    print(coins >= total_price(prices))


if __name__ == "__main__":
    basket = [12, 5, 30]
    print(f"Total: {total_price(basket)} coins")
    print(f"Cheapest item: {cheapest(basket)} coins")
    if can_buy(50, basket):
        print("With 50 coins you can buy everything!")
    else:
        print("With 50 coins you cannot buy everything.")
