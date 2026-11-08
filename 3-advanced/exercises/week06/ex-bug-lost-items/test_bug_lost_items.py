"""Checks for Bug Hunt 2 - Lost Scores."""


def test_keeps_every_score(load_target):
    game = load_target()
    result = game.sort_scores([40, 10, 30, 10, 50])
    assert len(result) == 5, f"5 scores went in but {len(result)} came out: {result}. Which ones got lost?"
    assert result == [10, 10, 30, 40, 50], f"Expected [10, 10, 30, 40, 50], got {result}."


def test_original_list_unchanged(load_target):
    game = load_target()
    scores = [3, 1, 2]
    game.sort_scores(scores)
    assert scores == [3, 1, 2], f"The original list changed to {scores}! Hint: remaining = scores does not make a copy."


def test_single_and_empty_lists(load_target):
    game = load_target()
    assert game.sort_scores([7]) == [7], "A list with one score should come back as [7]."
    assert game.sort_scores([]) == [], "An empty list should come back empty."
