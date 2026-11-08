"""Tests for the Maze Muncher turtle view (maze_muncher.py).

These run on a fake, invisible turtle screen: we press keys and run the
game clock by hand, then look at what the game did.
"""

import random
from pathlib import Path

from kidtest import load_module

HERE = Path(__file__).parent


def start_game(tmp_path, levels=None, nickname="Ada"):
    """Load the game (main block not run) and start it on a fake screen."""
    game_module = load_module(HERE / "maze_muncher.py")
    files = []
    for i, text in enumerate(levels or []):
        level = tmp_path / f"level{i + 1}.txt"
        level.write_text(text)
        files.append(level)
    app = game_module.start(nickname, files or None, tmp_path / "scores.txt")
    return app, game_module.turtle.screen


def all_texts(screen):
    return [t.text for pen in screen.turtle_list for t in pen.texts]


def test_start_draws_walls_letters_and_listens(tmp_path):
    app, screen = start_game(tmp_path)
    maze = app.game.maze
    walls = sum(maze.is_wall((r, c))
                for r in range(maze.height) for c in range(maze.width))
    assert len(app.wall_pen.fills) == walls, \
        "Every wall square should be drawn as a filled square."
    texts = all_texts(screen)
    for letter in "PGC":
        assert letter in texts, \
            f"Write the letter {letter} on its character (not color only)."
    arrows = {"Up", "Down", "Left", "Right"}
    assert screen.listening and arrows <= set(screen.key_handlers)
    assert screen.timers, "The game clock (ontimer) should be running."


def test_arrow_key_moves_and_eats(tmp_path):
    app, screen = start_game(tmp_path)
    screen.press("Right")
    assert app.game.player.pos == (1, 2)
    assert app.game.score == 10
    assert any("Score 10" in text for text in all_texts(screen)), \
        "The score on screen should update."


def test_clock_moves_ghosts_and_keeps_ticking(tmp_path):
    random.seed(1)
    app, screen = start_game(tmp_path)
    before = [ghost.pos for ghost in app.game.ghosts]
    ran = screen.run_timers(3)
    assert ran == 3, "Each tick should schedule the next one."
    after = [ghost.pos for ghost in app.game.ghosts]
    assert after != before, "The ghosts should move on each tick."


def test_caught_saves_high_score(tmp_path):
    app, screen = start_game(tmp_path, ["#####\n#P.C#\n#####\n"])
    screen.press("Right")  # eat one pellet, now next to the chaser
    screen.run_timers(5)
    assert app.game.state == "lost"
    assert "Ada,10" in (tmp_path / "scores.txt").read_text()
    assert "Caught" in app.message
    assert screen.timers == [], "The clock should stop when the game ends."


def test_clearing_a_level_and_moving_on(tmp_path):
    one_pellet = "####\n#P.#\n####\n"
    app, screen = start_game(tmp_path, [one_pellet, one_pellet])
    screen.press("Right")
    assert app.game.state == "won" and "SPACE" in app.message
    screen.press("space")
    assert app.level_index == 1 and app.game.state == "playing"
    screen.press("Right")
    assert "every level" in app.message
    saved = (tmp_path / "scores.txt").read_text()
    assert "Ada,20" in saved, "Scores from both levels add up."
    screen.press("r")
    assert app.level_index == 0 and app.game.score == 0
