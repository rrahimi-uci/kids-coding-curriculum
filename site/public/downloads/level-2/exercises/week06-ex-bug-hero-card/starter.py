# Bug Hunt Station 1: Hero Card
# This program has a bug. Press Run and read the error from the BOTTOM up:
#   1. the last line says WHAT went wrong,
#   2. the line above it shows WHERE (file name and line number).
# Fix the bug, run again, then run it again to check.


def card_line(label, value):
    """Return one line of the card, like "Level: 4"."""
    return label + ": " + value


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
