# Fix the Bugs the Tests Found
# Four small game helpers. Each one has ONE bug.
# Do not guess! Run it and look closely: the program shows you
# which function is broken and what they expected. Fix ONE function,
# run the checks again, and repeat.
# You can also read the tests themselves in test_fix_the_bugs.py.


def lives_after_hit(lives, damage):
    """Take damage away from lives, but never go below 0."""
    lives = lives - damage
    return lives


def medal(score):
    """100 or more: "gold". 50 to 99: "silver". Below 50: "bronze"."""
    if score > 100:
        return "gold"
    elif score > 50:
        return "silver"
    else:
        return "bronze"


def name_tag(nickname):
    """Return 'Player: ' and the nickname in capital letters."""
    print(f"Player: {nickname.upper()}")


def average_score(scores):
    """Return the average of the scores, rounded to a whole number.
    An empty list gives 0."""
    return round(sum(scores) / len(scores))


if __name__ == "__main__":
    print(lives_after_hit(3, 1))       # 2
    print(lives_after_hit(1, 5))       # 0
    print(medal(100), medal(50))       # gold silver
    print(name_tag("pixel"))           # Player: PIXEL
    print(average_score([10, 20, 40]))  # 23
    print(average_score([]))           # 0
