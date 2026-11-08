# TEACHER REFERENCE SOLUTION: Exercise 8.3 - Fix the Bugs the Tests Found
#
# What it does: four small game helpers (lives after a hit, medal for a
# score, a name tag, an average score). Each one had exactly ONE bug that a
# ready-made test finds.
# Key ideas: reading a failing test as a clue, boundary values (is exactly
# 100 gold?), "return" versus "print", and protecting against dividing by zero.
# Approach: fix one function at a time, guided by what each test expected.
# The four fixes are marked FIX 1 to FIX 4 below.


def lives_after_hit(lives, damage):
    """Take damage away from lives, but never go below 0."""
    lives = lives - damage
    # FIX 1: the starter returned the sum as it was, so 1 life minus 5 damage
    # gave -4. A player cannot have negative lives, so we stop at 0.
    if lives < 0:
        lives = 0
    return lives


def medal(score):
    """100 or more: "gold". 50 to 99: "silver". Below 50: "bronze"."""
    # FIX 2: the starter used ">" (strictly more than), so exactly 100 and
    # exactly 50 fell into the wrong medal. ">=" means "this or more", which
    # is what "100 or more" says. The check goes from the highest medal down.
    if score >= 100:
        return "gold"
    elif score >= 50:
        return "silver"
    else:
        return "bronze"


def name_tag(nickname):
    """Return 'Player: ' and the nickname in capital letters."""
    # FIX 3: the starter used print(), which only shows text on the screen
    # and gives back nothing (None). "return" hands the text to the caller,
    # who can then print it, store it or test it.
    return f"Player: {nickname.upper()}"


def average_score(scores):
    """Return the average of the scores, rounded to a whole number.
    An empty list gives 0."""
    # FIX 4: with no scores, len(scores) is 0 and dividing by 0 crashes
    # (ZeroDivisionError). We check for the empty list first and answer 0.
    if len(scores) == 0:
        return 0
    return round(sum(scores) / len(scores))


if __name__ == "__main__":
    print(lives_after_hit(3, 1))       # 2
    print(lives_after_hit(1, 5))       # 0
    print(medal(100), medal(50))       # gold silver
    print(name_tag("pixel"))           # Player: PIXEL
    print(average_score([10, 20, 40]))  # 23
    print(average_score([]))           # 0


# Common mistakes children make here:
# - Changing the test instead of the function. The test describes what the
#   function SHOULD do, so the function is what needs fixing.
# - In medal(), changing only one of the two ">" signs, so exactly 100 is
#   fixed but exactly 50 is still wrong (or the other way around).
# - In name_tag(), keeping the print() and adding a "return" below it: the
#   name then prints twice in the main program.
# - In lives_after_hit(), putting the "below 0" check before the subtraction,
#   when lives is still positive.
#
# Another correct way: max() picks the bigger of two numbers, so
#     return max(0, lives - damage)
# does the whole of lives_after_hit() in one line.
