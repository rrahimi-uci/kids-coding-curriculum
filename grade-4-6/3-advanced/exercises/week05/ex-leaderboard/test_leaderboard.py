"""Checks for Exercise 5.2 - Leaderboard."""

SCORES = [("Ada", 120), ("Leo", 95), ("Mei", 150), ("Omar", 95), ("Zoe", 80)]


def test_top_scores(load_target):
    board = load_target()
    top = board.top_scores(SCORES, 3)
    assert top == [("Mei", 150), ("Ada", 120), ("Leo", 95)], f"The top 3 should be Mei, Ada, Leo. Got {top}"
    assert len(board.top_scores(SCORES, 1)) == 1, "top_scores(scores, 1) should return only 1 entry."


def test_alphabetical_ignores_capitals(load_target):
    board = load_target()
    names = [entry[0] for entry in board.alphabetical([("zoe", 1), ("Ada", 2), ("mei", 3), ("Kai", 4)])]
    assert names == ["Ada", "Kai", "mei", "zoe"], f"A to Z (ignoring capitals) should be Ada, Kai, mei, zoe. Got {names}"


def test_ties_share_a_place(load_target):
    board = load_target()
    lines = board.rank_lines(SCORES)
    assert lines == ["1. Mei - 150", "2. Ada - 120", "3. Leo - 95", "3. Omar - 95", "5. Zoe - 80"], (
        f"Leo and Omar both have 95, so they share 3rd place and Zoe is 5th. Got {lines}"
    )


def test_original_scores_unchanged(load_target):
    board = load_target()
    scores = list(SCORES)
    board.top_scores(scores)
    board.alphabetical(scores)
    board.rank_lines(scores)
    assert scores == SCORES, "sorted() makes a new list - the original scores should not change."
