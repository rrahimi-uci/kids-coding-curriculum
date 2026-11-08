# Game Math - reference solution
# Three small functions that RETURN an answer, so the rest of the game
# can use it. A function that only prints shows the answer on the screen,
# but hands nothing back.


def xp_needed(level):
    """Return how many experience points (XP) you need to reach this level."""
    return level * 100


def damage(attack, shield):
    """Return the damage a hit does. The shield blocks some of the attack,
    but damage can never be less than 0."""
    result = attack - shield
    if result < 0:
        result = 0
    return result


def is_critical(roll):
    """Return True if a 20-sided dice roll is a critical hit (19 or 20)."""
    return roll >= 19


if __name__ == "__main__":
    print(f"To reach level 5 you need {xp_needed(5)} XP.")
    hit = damage(12, 5)
    print(f"The dragon attacks with 12 against your shield of 5: {hit} damage!")
    blocked = damage(3, 5)
    print(f"The goblin attacks with 3 against your shield of 5: {blocked} damage.")
    health = 40 - hit - blocked        # we can do math with returned values
    print(f"Health left: {health}")
    for roll in [7, 19, 20]:
        print(f"Roll {roll}: critical hit? {is_critical(roll)}")
