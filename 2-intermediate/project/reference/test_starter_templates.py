"""Teacher check: the starter templates in ../starter run, react to keys and
their example tests pass, so students start from something that works."""

from pathlib import Path

from kidtest import load_module

STARTER = Path(__file__).parent.parent / "starter"


def test_game_template_moves_scores_and_times_out():
    game = load_module(STARTER / "game_template.py")
    game.start_game()
    screen = game.turtle.screen
    screen.press("Right")
    assert game.view["player"].xcor() == game.SETTINGS["step"]
    coin = game.view["coin"]
    game.view["player"].goto(coin.xcor(), coin.ycor())
    screen.run_timers(1)
    assert game.game["score"] == 1, "Touching the coin should score a point."
    screen.run_timers(2000)
    assert not game.game["running"], "The countdown should end the game."
    assert screen.timers == [], "Nothing should keep running after TIME UP."


def test_art_template_draws_and_saves(tmp_path):
    art = load_module(STARTER / "art_studio_template.py")
    art.SAVE_FILE = tmp_path / "my_design.txt"
    art.start_studio()
    screen = art.turtle.screen
    assert len(art.view["artist"].lines) > 20, "A design should be drawn at the start."
    screen.press("n")
    screen.press("s")
    assert art.SAVE_FILE.read_text().startswith("petals=")
    screen.press("l")   # the TODO version must not crash


def test_example_student_tests_pass():
    tests = load_module(STARTER / "my_tests.py")
    names = [n for n in dir(tests) if n.startswith("test_")]
    assert len(names) >= 3
    for name in names:
        getattr(tests, name)()
