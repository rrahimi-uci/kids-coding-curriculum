# Fix the Bugs the Tests Found - reference solution
# Four small game helpers. Each one had ONE bug; the fix is marked FIXED.


def lives_after_hit(lives, damage):
    """Take damage away from lives, but never go below 0."""
    lives = lives - damage
    if lives < 0:  # FIXED: lives can never be negative
        lives = 0
    return lives


def medal(score):
    """100 or more: "gold". 50 to 99: "silver". Below 50: "bronze"."""
    if score >= 100:  # FIXED: >= so that exactly 100 is gold
        return "gold"
    elif score >= 50:  # FIXED: >= so that exactly 50 is silver
        return "silver"
    else:
        return "bronze"


def name_tag(nickname):
    """Return 'Player: ' and the nickname in capital letters."""
    return f"Player: {nickname.upper()}"  # FIXED: return, not print


def average_score(scores):
    """Return the average of the scores, rounded to a whole number.
    An empty list gives 0."""
    if len(scores) == 0:  # FIXED: no dividing by zero
        return 0
    return round(sum(scores) / len(scores))


if __name__ == "__main__":
    print(lives_after_hit(3, 1))       # 2
    print(lives_after_hit(1, 5))       # 0
    print(medal(100), medal(50))       # gold silver
    print(name_tag("pixel"))           # Player: PIXEL
    print(average_score([10, 20, 40]))  # 23
    print(average_score([]))           # 0
