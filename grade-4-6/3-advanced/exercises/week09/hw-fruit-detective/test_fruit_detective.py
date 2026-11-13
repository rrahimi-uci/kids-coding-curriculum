"""Checks for Homework 9 - Fruit detective (k-nearest neighbors)."""

CARDS = [(0, 0, "a"), (10, 10, "b"), (1, 1, "c"), (5, 5, "d")]


def test_k_nearest_gives_the_closest_cards_in_order(load_target):
    program = load_target()
    got = program.k_nearest(CARDS, (0, 1), 2)
    assert got == [(0, 0, "a"), (1, 1, "c")], f"The 2 closest cards to (0, 1) are a then c, not {got}."
    assert len(program.k_nearest(CARDS, (0, 0), 3)) == 3, "k_nearest(..., 3) should give exactly 3 cards."


def test_vote(load_target):
    program = load_target()
    assert program.vote(["lemon", "apple", "lemon"]) == "lemon", "2 votes for lemon beat 1 vote for apple."
    assert program.vote(["grape"]) == "grape", "With one vote, that label wins."
    assert program.vote(["apple", "grape"]) == "apple", "In a tie, the first label in the list wins."


def test_voting_beats_one_wrong_card(load_target):
    program = load_target()
    mystery = (5, 4)
    assert program.classify(program.TRAINING, mystery, k=1) == "apple", \
        "With k = 1 the sorter copies the wrongly-labeled card next to (5, 4)."
    assert program.classify(program.TRAINING, mystery, k=3) == "lemon", \
        "With k = 3 the two real lemons should outvote the wrong card."
