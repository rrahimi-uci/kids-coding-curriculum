# TEACHER REFERENCE SOLUTION: Hero Card (Exercise 1.1)
#
# What the program does: it asks the child for a made-up hero name, a super
# power and a level, then prints a neat character card.
# Key ideas practiced: the four data types (text, whole number, decimal number,
# True/False), turning typed text into a number with int(), and f-strings.
# Approach: the bug in the starter is that input() always gives back TEXT, so
# we convert the level with int() once, where it is typed (TODO 1, part 1).
# The "Next level" line also glued text and a number with +, so it becomes an
# f-string (TODO 1, part 2). After that the math works, and the card is printed
# with f-strings (a string that starts with f and shows variables inside { } ).
#
# The card uses all four data types:
#   str   (text)            hero_name, power
#   int   (whole number)    level, power_points
#   float (decimal number)  health
#   bool  (True or False)   is_legend


def print_card(hero_name, power, level):
    """Print a character card for one hero."""
    power_points = level * 10      # whole number times whole number gives a whole number
    health = level * 12.5          # a decimal number in the sum makes the answer a decimal
    is_legend = level >= 10        # a comparison always gives True or False
    print("+------------------------------+")
    print(f"  HERO:         {hero_name}")
    print(f"  Power:        {power}")
    print(f"  Level:        {level}")
    # FIX 1, part 2: the starter wrote "  Next level:   " + level + 1. Even with
    # level as a number that crashes, because Python cannot glue text and a
    # number with +. The f-string turns the number into text for us. level is a
    # number now, so level + 1 inside the braces is real addition (4 becomes 5).
    print(f"  Next level:   {level + 1}")
    print(f"  Power points: {power_points}")
    print(f"  Health:       {health}")
    print(f"  Legend?       {is_legend}")
    print("+------------------------------+")


# This part runs only when you press Run on THIS file.
if __name__ == "__main__":
    print("Welcome to the Hero Card Maker!")
    hero_name = input("Hero name (make one up - not your real name): ")
    power = input("Super power: ")
    # FIX 1, part 1: input() always gives back text, so level + 1 crashed (TypeError).
    # int() turns the typed text into a whole number before we use it in math.
    level = int(input("Level (a whole number, 1 to 20): "))
    print_card(hero_name, power, level)


# Common mistakes children make here:
# - Fixing the crash in the wrong place, for example writing int(level) + 1 but
#   leaving level as text, so the later math (level * 10) prints "4444444444".
#   Convert once, right after input().
# - Typing a decimal such as 4.5 for the level: int() only accepts whole numbers
#   and shows a ValueError. That is fine for now; talk about why.
# - Forgetting the f in front of the quotes, so the card prints the words
#   {hero_name} instead of the name.
# - Writing is_legend = "level >= 10" in quotes, which makes text instead of
#   True/False.
#
# Another correct way: skip the extra variables and put the math inside the braces.
#   print(f"  Power points: {level * 10}")
#   print(f"  Health:       {level * 12.5}")
