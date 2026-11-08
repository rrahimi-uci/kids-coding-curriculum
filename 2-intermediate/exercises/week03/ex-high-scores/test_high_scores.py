"""Checks for Exercise 3.3 - Top 3 High Scores."""


def test_top_three_are_the_best_three(load_target):
    m = load_target()
    answer = m.top_three([120, 45, 300, 80])
    assert answer == [300, 120, 80], f"The best three of [120, 45, 300, 80] are [300, 120, 80], not {answer}."


def test_top_three_with_only_two_scores(load_target):
    m = load_target()
    answer = m.top_three([10, 70])
    assert answer == [70, 10], f"With only two scores, return both, biggest first: [70, 10], not {answer}."


def test_leaderboard_shows_places(run_target):
    out = run_target(inputs=["500"]).stdout
    assert "1st: 300" in out, "The first leaderboard should start with '1st: 300'. See TODO 2."
    assert "1st: 500" in out, "After scoring 500, the new leaderboard should start with '1st: 500'."
    assert "45" not in out.split("New leaderboard")[-1], "Only the top 3 should be shown: 45 is not in the top 3."
