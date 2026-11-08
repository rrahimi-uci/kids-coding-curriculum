"""Checks for Exercise 8.3 - Fix the Bugs the Tests Found.

Read a test like a sentence: "lives_after_hit(1, 5) should be 0".
If it fails, the function it calls has a bug.
"""


def test_lives_never_go_below_zero(load_target):
    game = load_target()
    assert game.lives_after_hit(3, 1) == 2, "3 lives, hit for 1, should leave 2 lives."
    result = game.lives_after_hit(1, 5)
    assert result == 0, f"1 life, hit for 5, should leave 0 lives, not {result}. Lives can never be negative."


def test_medals_on_the_boundaries(load_target):
    game = load_target()
    assert game.medal(150) == "gold" and game.medal(20) == "bronze", "150 is gold and 20 is bronze."
    assert game.medal(100) == "gold", f"Exactly 100 should be gold, not {game.medal(100)!r}. Check > and >=."
    assert game.medal(50) == "silver", f"Exactly 50 should be silver, not {game.medal(50)!r}. Check > and >=."


def test_name_tag_returns_the_text(load_target):
    game = load_target()
    tag = game.name_tag("pixel")
    assert tag == "Player: PIXEL", (
        f"name_tag('pixel') should RETURN 'Player: PIXEL', but it gave back {tag!r}. "
        "print() shows text on the screen; return hands it back to the code."
    )


def test_average_score(load_target):
    game = load_target()
    assert game.average_score([10, 20, 40]) == 23, "The average of 10, 20 and 40 is 70 / 3, which rounds to 23."


def test_average_of_no_scores_is_zero(load_target):
    game = load_target()
    try:
        result = game.average_score([])
    except ZeroDivisionError:
        raise AssertionError("average_score([]) crashed with ZeroDivisionError. An empty list should give 0.")
    assert result == 0, f"average_score([]) should give 0, not {result}."
