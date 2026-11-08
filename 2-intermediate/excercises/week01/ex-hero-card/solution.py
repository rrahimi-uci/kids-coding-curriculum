# Hero Card - reference solution
# Ask for a made-up hero name, a super power and a level, then print a
# character card. The card uses all four data types:
#   str   (text)            hero_name, power
#   int   (whole number)    level, power_points
#   float (decimal number)  health
#   bool  (True or False)   is_legend


def print_card(hero_name, power, level):
    """Print a character card for one hero."""
    power_points = level * 10      # int times int gives an int
    health = level * 12.5          # int times float gives a float
    is_legend = level >= 10        # a comparison gives a bool
    print("+------------------------------+")
    print(f"  HERO:         {hero_name}")
    print(f"  Power:        {power}")
    print(f"  Level:        {level}")
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
    # int() turns the typed text into a whole number
    level = int(input("Level (a whole number, 1 to 20): "))
    print_card(hero_name, power, level)
