# Hero Card
# Press Run (F5). Oh no - a red error! That is this week's bug hunt.
# Read the LAST line of the error first. Then fix the TODOs one at a time.


def print_card(hero_name, power, level):
    """Print a character card for one hero."""
    power_points = level * 10
    print("+------------------------------+")
    print(f"  HERO:         {hero_name}")
    # TODO 2: add a line that shows the power, like the HERO line above.
    print(f"  Level:        {level}")
    # TODO 1, part 2: this line glues text and a number together with "+",
    #         which still crashes after part 1. Write it as an f-string too.
    print("  Next level:   " + level + 1)
    # TODO 3: show power_points with an f-string.
    # TODO 4: make a variable health = level * 12.5 and show it.
    # TODO 5: make a variable is_legend = level >= 10 and show it
    #         with the label "Legend?".
    print("+------------------------------+")


# This part runs only when you press Run on THIS file.
if __name__ == "__main__":
    print("Welcome to the Hero Card Maker!")
    hero_name = input("Hero name (make one up - not your real name): ")
    power = input("Super power: ")
    # TODO 1, part 1: input() always gives back TEXT. Turn it into a whole number.
    level = input("Level (a whole number, 1 to 20): ")
    print_card(hero_name, power, level)
