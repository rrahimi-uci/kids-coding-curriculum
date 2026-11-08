# TEACHER REFERENCE SOLUTION: Bug Hunt Station 1 - Hero Card
#
# What it does: builds the lines of a hero card ("Hero: Zoe the Brave",
# "Level: 4", ...) and prints them.
# Key ideas: reading a traceback from the bottom up, and the difference
# between text (str) and numbers (int).
# Approach: the starter joined a label and a value with "+". That works for
# two pieces of text but crashes (TypeError) when the value is a number.
# An f-string turns any value into text for us.


def card_line(label, value):
    """Return one line of the card, like "Level: 4"."""
    # FIX 1: "label + ': ' + value" crashed with a TypeError when value was a
    # number (Python will not add text and a number). The f-string converts
    # the value to text itself, so it works for names and numbers alike.
    return f"{label}: {value}"


def make_card(name, level, coins):
    """Return a list of card lines for a hero."""
    return [
        card_line("Hero", name),
        card_line("Level", level),
        card_line("Coins", coins),
        # level + 1 is real arithmetic on a number; card_line turns the
        # result into text afterwards.
        card_line("Next level", level + 1),
    ]


if __name__ == "__main__":
    for line in make_card("Zoe the Brave", 4, 120):
        print(line)


# Common mistakes children make here:
# - Fixing only one call, e.g. writing str(level) inside make_card for the
#   "Level" line but forgetting "Coins" and "Next level". One fix inside
#   card_line covers every line.
# - Writing str(level + 1) as str(level) + 1, which is still text + number.
# - Putting quotes round the whole thing, e.g. "{label}: {value}" without
#   the f in front, which prints the curly brackets literally.
#
# Another correct way: convert the value to text with str():
#     return label + ": " + str(value)
