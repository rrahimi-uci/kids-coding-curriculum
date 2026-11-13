"""Tests for the Star Catcher window (star_catcher.py) on the fake turtle
screen: press keys, run the timer, and check what the player would see."""

from pathlib import Path

from kidtest import load_module

HERE = Path(__file__).parent


def start(tmp_path):
    """Load the game and start it with a score file in tmp_path."""
    module = load_module(HERE / "star_catcher.py")
    module.start_game(tmp_path / "scores.txt")
    return module, module.turtle.screen


def hud_texts(module):
    return " ".join(t.text for t in module.view["hud"].texts)


def test_window_listens_for_the_arrow_keys(tmp_path):
    module, screen = start(tmp_path)
    assert screen.listening, "Call screen.listen() or keys do nothing."
    assert "Left" in screen.key_handlers
    assert "Right" in screen.key_handlers


def test_arrow_keys_move_the_basket(tmp_path):
    module, screen = start(tmp_path)
    step = module.SETTINGS["basket_step"]
    screen.press("Left")
    screen.press("Left")
    assert module.game["basket_x"] == -2 * step
    screen.press("Right")
    assert module.game["basket_x"] == -step


def test_timer_keeps_the_game_running(tmp_path):
    module, screen = start(tmp_path)
    ran = screen.run_timers(30)
    assert ran == 30, "The game loop should schedule itself with ontimer."
    assert module.game["ticks"] == 30
    assert len(module.game["objects"]) >= 1, \
        "Stars or meteors should start falling."


def test_catching_a_star_shows_a_higher_score(tmp_path):
    module, screen = start(tmp_path)
    basket_y = module.SETTINGS["basket_y"]
    star = {"kind": "star", "x": 0, "y": basket_y + 10}
    module.game["objects"].append(star)
    screen.run_timers(1)
    assert module.game["score"] == 1
    assert "Score: 1" in hud_texts(module), \
        "The score on screen should go up."


def test_game_over_saves_the_score_and_space_restarts(tmp_path):
    module, screen = start(tmp_path)
    basket_y = module.SETTINGS["basket_y"]
    module.game["score"] = 6
    module.game["lives"] = 1
    meteor = {"kind": "meteor", "x": 0, "y": basket_y}
    module.game["objects"].append(meteor)
    screen.run_timers(5)
    assert module.game["game_over"], \
        "Touching a meteor with 1 life left should end the game."
    assert "GAME OVER" in hud_texts(module)
    saved = (tmp_path / "scores.txt").read_text().split()
    assert saved == ["6"], "The score should be saved in the file."
    assert screen.run_timers(5) == 0, "After game over the loop stops."

    screen.press("space")
    assert module.game["score"] == 0, "Space starts a new game."
    assert not module.game["game_over"]
    assert screen.run_timers(3) == 3
