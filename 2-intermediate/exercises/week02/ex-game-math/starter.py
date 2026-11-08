# Game Math
# Run this first and read what it prints. Something strange happens with
# xp_needed: it shows a number AND the word None. Why? (Bug hunt!)


def xp_needed(level):
    """Return how many experience points (XP) you need to reach this level."""
    # TODO 1: this function PRINTS the answer but does not hand it back.
    print(level * 100)


def damage(attack, shield):
    """Return the damage a hit does. The shield blocks some of the attack,
    but damage can never be less than 0."""
    result = attack - shield
    # TODO 2: if result is less than 0, make it 0.
    # TODO 3: hand result back with return.


def is_critical(roll):
    """Return True if a 20-sided dice roll is a critical hit (19 or 20)."""
    # TODO 4: return True for 19 or 20, otherwise False.
    return False


if __name__ == "__main__":
    print(f"To reach level 5 you need {xp_needed(5)} XP.")
    hit = damage(12, 5)
    print(f"The dragon attacks with 12 against your shield of 5: {hit} damage!")
    blocked = damage(3, 5)
    print(f"The goblin attacks with 3 against your shield of 5: {blocked} damage.")
    # TODO 5: when TODO 3 is done, remove the # at the start of the next two lines.
    # health = 40 - hit - blocked
    # print(f"Health left: {health}")
    for roll in [7, 19, 20]:
        print(f"Roll {roll}: critical hit? {is_critical(roll)}")
