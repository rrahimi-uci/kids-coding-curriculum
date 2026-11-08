# TEACHER REFERENCE SOLUTION: Game Math (Exercise 2.1)
#
# What the program does: it works out game numbers (XP needed for a level,
# damage after a shield, and whether a dice roll is a critical hit) and prints
# a short battle report.
# Key idea practiced: return versus print. A function that only prints shows the
# answer on the screen but hands nothing back, so the rest of the program gets
# the special value None. A function that returns hands the answer to the caller.
# Approach: each function does its small job and returns the result. The bottom
# of the file then uses those returned values, for example in the health sum.


def xp_needed(level):
    """Return how many experience points (XP) you need to reach this level."""
    # FIX 1: the starter used print() here, so the caller received None and the
    # message said "you need None XP". return hands the number back instead.
    return level * 100


def damage(attack, shield):
    """Return the damage a hit does. The shield blocks some of the attack,
    but damage can never be less than 0."""
    result = attack - shield
    if result < 0:               # a strong shield must not heal the monster
        result = 0
    return result


def is_critical(roll):
    """Return True if a 20-sided dice roll is a critical hit (19 or 20)."""
    # The comparison itself is True or False, so we can return it directly.
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


# Common mistakes children make here:
# - Keeping print(...) and just adding return on another line, so the number is
#   shown twice; the print line should be replaced by the return.
# - Forgetting the final "return result" in damage(): the function then quietly
#   returns None and the health sum crashes with a TypeError.
# - Writing is_critical as "if roll >= 19: return True" with no else/return False;
#   a miss then gives None instead of False (the tests check for False).
# - Using "roll > 19" which misses a roll of exactly 19.
#
# Another correct way: max() picks the bigger of two numbers, so damage can be
# written in one line.
#   return max(attack - shield, 0)
