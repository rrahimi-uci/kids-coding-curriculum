"""Tests for the Maze Muncher game logic (muncher_model.py).

Run them in Terminal from this folder with:   python3 -m pytest -q
"""

import random
from pathlib import Path

from kidtest import load_module

HERE = Path(__file__).parent
model = load_module(HERE / "muncher_model.py")

# A tiny level used by several tests. Row 0 is the top line.
#   col: 01234
SMALL = ["#####",
         "#P..#",
         "#.#.#",
         "#..G#",
         "#####"]


def make_game(lines):
    return model.Game(model.Maze(lines))


# ---------------------------------------------------- level files
def test_parsing_finds_size_and_starts():
    maze = model.Maze(SMALL)
    assert (maze.width, maze.height) == (5, 5)
    assert maze.starts["P"] == [(1, 1)], "P is on row 1, column 1."
    assert maze.starts["G"] == [(3, 3)]
    assert maze.is_wall((0, 0)) and not maze.is_wall((1, 2))


def test_start_squares_hold_pellets_except_the_players():
    maze = model.Maze(SMALL)
    assert not maze.has_pellet((1, 1)), "The player starts on an empty square."
    assert maze.has_pellet((3, 3)), "A ghost starts on top of a pellet."
    assert maze.pellets_left() == 7, "2 + 2 + 3 pellets (one under the ghost)."


def test_short_rows_are_padded_with_walls():
    maze = model.Maze(["####", "#P.", "####"])
    assert maze.width == 4
    assert maze.is_wall((1, 3)), "A missing square at a row end is a wall."


def test_a_level_needs_exactly_one_player():
    for bad in (["#..#"], ["#PP#"]):
        try:
            model.Maze(bad)
        except ValueError:
            continue
        raise AssertionError(f"Maze({bad}) needs exactly one P: ValueError.")


def test_every_shipped_level_has_reachable_pellets():
    for level in sorted((HERE / "levels").glob("*.txt")):
        maze = model.load_maze(level)
        player = maze.starts["P"][0]
        for row in range(maze.height):
            for col in range(maze.width):
                if maze.has_pellet((row, col)):
                    path = maze.shortest_path(player, (row, col))
                    assert path, \
                        f"{level.name}: pellet {(row, col)} cannot be reached."


# ---------------------------------------------------- moving and eating
def test_walls_block_moves():
    game = make_game(SMALL)
    game.move_player("up")
    assert game.player.pos == (1, 1), "A wall above should stop the player."
    assert not game.player.try_move(game.maze, "left")


def test_eating_a_pellet_scores_once():
    game = make_game(SMALL)
    game.move_player("right")
    assert game.player.pos == (1, 2)
    assert game.score == 10 and not game.maze.has_pellet((1, 2))
    game.move_player("left")
    game.move_player("right")
    assert game.score == 10, "A pellet can only be eaten once."


# ---------------------------------------------------- breadth-first search
def test_bfs_straight_corridor():
    maze = model.Maze(["#######", "#P....#", "#######"])
    path = maze.shortest_path((1, 1), (1, 5))
    assert path[0] == (1, 1) and path[-1] == (1, 5)
    assert len(path) == 5, "4 steps apart, so the path has 5 squares."


def test_bfs_goes_around_a_wall():
    maze = model.Maze(SMALL)
    path = maze.shortest_path((1, 1), (3, 3))
    assert len(path) - 1 == 4, "The shortest way round the wall is 4 steps."
    for a, b in zip(path, path[1:]):
        steps = abs(a[0] - b[0]) + abs(a[1] - b[1])
        assert steps == 1, "Each step moves exactly one square."
        assert not maze.is_wall(b)


def test_bfs_unreachable_target_gives_empty_path():
    maze = model.Maze(["#####", "#P#.#", "#####"])
    assert maze.shortest_path((1, 1), (1, 3)) == []


# ---------------------------------------------------- ghosts
def test_chaser_takes_one_step_closer():
    game = make_game(["#######", "#P...C#", "#######"])
    chaser = game.ghosts[0]
    assert isinstance(chaser, model.Chaser) and isinstance(chaser, model.Ghost)
    before = len(game.maze.shortest_path(chaser.pos, game.player.pos))
    game.tick()
    after = len(game.maze.shortest_path(chaser.pos, game.player.pos))
    assert chaser.pos == (1, 4) and after == before - 1


def test_ghost_wanders_only_onto_open_squares_and_does_not_turn_back():
    random.seed(3)
    maze = model.Maze(SMALL)
    ghost = model.Ghost((3, 3))
    for _ in range(20):
        old = ghost.pos
        ghost.take_turn(maze, (1, 1))
        assert not maze.is_wall(ghost.pos)
        assert ghost.pos in maze.neighbors(old)
    # In a corridor with no dead end the ghost keeps going forwards.
    corridor = model.Maze(["#######", "#P....#", "#######"])
    ghost = model.Ghost((1, 3))
    ghost.previous = (1, 2)
    ghost.take_turn(corridor, (1, 1))
    assert ghost.pos == (1, 4), "A ghost only turns back when it is stuck."


# ---------------------------------------------------- win and lose
def test_win_when_all_pellets_are_eaten():
    game = make_game(["#####", "#P.##", "#####"])
    game.move_player("right")
    assert game.state == "won"
    game.move_player("left")
    assert game.player.pos == (1, 2), "After winning, the player stops moving."


def test_lose_when_a_ghost_catches_you():
    game = make_game(["######", "#P.C.#", "######"])
    game.tick()  # the chaser steps next to the player...
    game.tick()  # ...and then onto the player
    assert game.state == "lost"


# ---------------------------------------------------- high scores
def test_high_score_file_is_created_and_round_trips(tmp_path):
    scores_file = tmp_path / "scores.txt"
    assert model.load_high_scores(scores_file) == []
    assert scores_file.exists(), "A missing high-score file should be created."
    model.add_high_score(scores_file, "Ada", 50)
    model.add_high_score(scores_file, "Kai", 120)
    assert model.load_high_scores(scores_file) == [("Kai", 120), ("Ada", 50)]


def test_only_the_best_five_are_kept_and_bad_lines_are_skipped(tmp_path):
    scores_file = tmp_path / "scores.txt"
    scores_file.write_text("Mei,30\nnot a score\n\nOmar,x\n")
    for points in [10, 90, 40, 70, 20]:
        model.add_high_score(scores_file, "Leo", points)
    best = model.load_high_scores(scores_file)
    assert [p for _, p in best] == [90, 70, 40, 30, 20]
