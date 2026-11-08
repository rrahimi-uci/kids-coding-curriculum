# Bug Hunt Station 1: Hero Card - FIXED version (teacher)
# Bug: card_line() glued text and a number together with +.
# Fix: an f-string turns any value into text for us.


def card_line(label, value):
    """Return one line of the card, like "Level: 4"."""
    return f"{label}: {value}"


def make_card(name, level, coins):
    """Return a list of card lines for a hero."""
    return [
        card_line("Hero", name),
        card_line("Level", level),
        card_line("Coins", coins),
        card_line("Next level", level + 1),
    ]


if __name__ == "__main__":
    for line in make_card("Zoe the Brave", 4, 120):
        print(line)
