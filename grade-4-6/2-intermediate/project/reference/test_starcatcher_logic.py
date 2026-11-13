"""Tests for the Star Catcher rules (starcatcher_logic.py).

Each test checks ONE rule with small, made-up numbers. Files are written
into pytest's tmp_path folder, so the real high-score file is safe.
"""

import random
from pathlib import Path

from kidtest import load_module

logic = load_module(Path(__file__).parent / "starcatcher_logic.py")
SETTINGS = logic.SETTINGS


def test_basket_moves_one_step_left_and_right():
    step = SETTINGS["basket_step"]
    assert logic.move_basket(0, -1, SETTINGS) == -step, \
        "Left should take one step to the left."
    assert logic.move_basket(0, 1, SETTINGS) == step, \
        "Right should take one step to the right."


def test_basket_stops_at_the_walls():
    left, right = SETTINGS["left_wall"], SETTINGS["right_wall"]
    assert logic.move_basket(left, -1, SETTINGS) == left, \
        "The basket slid through the left wall."
    assert logic.move_basket(right, 1, SETTINGS) == right, \
        "The basket slid through the right wall."


def test_step_objects_moves_everything_down():
    star = logic.make_object("star", 10, SETTINGS)
    meteor = logic.make_object("meteor", -50, SETTINGS)
    moved = logic.step_objects([star, meteor], 5)
    top = SETTINGS["top_y"]
    assert [o["y"] for o in moved] == [top - 5, top - 5], \
        "Everything should fall by 5."
    assert [o["kind"] for o in moved] == ["star", "meteor"], \
        "Stars must stay stars and meteors must stay meteors."
    assert star["y"] == top, "step_objects should not change the old list."


def test_caught_only_when_close_to_the_basket():
    basket_y = SETTINGS["basket_y"]
    near = {"kind": "star", "x": 10, "y": basket_y + 5}
    far = {"kind": "star", "x": 200, "y": basket_y}
    high = {"kind": "star", "x": 0, "y": 0}
    assert logic.is_caught(near, 0, SETTINGS), \
        "A star right next to the basket should be caught."
    assert not logic.is_caught(far, 0, SETTINGS), \
        "A star far to the side should be missed."
    assert not logic.is_caught(high, 0, SETTINGS), \
        "A star high in the sky is not caught yet."


def test_stars_score_points_and_meteors_do_not():
    assert logic.update_score(4, "star") == 5
    assert logic.update_score(4, "meteor") == 4


def test_tick_catches_a_star_and_removes_it():
    game = logic.new_game(SETTINGS)
    star = {"kind": "star", "x": 0, "y": SETTINGS["basket_y"] + 10}
    game["objects"].append(star)
    logic.tick(game, SETTINGS)
    assert game["score"] == 1, "Catching a star should give 1 point."
    assert game["objects"] == [], "A caught star should disappear."


def test_meteors_cost_lives_and_end_the_game():
    game = logic.new_game(SETTINGS)
    game["lives"] = 1
    meteor = {"kind": "meteor", "x": 0, "y": SETTINGS["basket_y"]}
    game["objects"].append(meteor)
    logic.tick(game, SETTINGS)
    assert game["lives"] == 0
    assert game["game_over"], "With no lives left the game should be over."


def test_fallen_objects_are_removed():
    game = logic.new_game(SETTINGS)
    star = {"kind": "star", "x": 200, "y": SETTINGS["bottom_y"]}
    game["objects"].append(star)
    logic.tick(game, SETTINGS)
    assert game["objects"] == [], \
        "Things below the bottom of the screen should be removed."
    assert game["score"] == 0
    assert game["lives"] == SETTINGS["start_lives"]


def test_new_objects_appear_at_the_top_over_time():
    random.seed(3)
    game = logic.new_game(SETTINGS)
    for _ in range(SETTINGS["spawn_every"]):
        logic.tick(game, SETTINGS)
    assert len(game["objects"]) == 1, \
        "One new thing should appear every spawn_every ticks."
    assert game["objects"][0]["kind"] in ("star", "meteor")


def test_missing_score_file_gives_empty_list(tmp_path):
    missing = tmp_path / "nothing_here.txt"
    assert logic.load_high_scores(missing) == []


def test_scores_are_saved_and_loaded_best_first(tmp_path):
    filename = tmp_path / "scores.txt"
    logic.save_high_scores(filename, [3, 12, 7])
    assert filename.exists(), "save_high_scores should create the file."
    assert logic.load_high_scores(filename) == [12, 7, 3]


def test_broken_lines_in_the_score_file_are_skipped(tmp_path):
    filename = tmp_path / "scores.txt"
    filename.write_text("8\n\nbanana\n15\n")
    assert logic.load_high_scores(filename) == [15, 8]


def test_add_score_keeps_only_the_best():
    assert logic.add_score([9, 5, 2], 7, 3) == [9, 7, 5]
    assert logic.add_score([], 4, 5) == [4]
