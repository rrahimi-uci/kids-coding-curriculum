"""Example tests for the three starter templates.

1. Keep the section for the option you chose and delete the other two.
2. When you rename your program, change the import line to match.
3. Add your OWN tests until you have at least 5 (the project needs 5+).
   A good test: set something up, do ONE thing, then assert what you expect.

Run them in Terminal, from your project folder:   python3 -m pytest -q
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # so Python finds the programs in this folder

# ---------------------------------------------------------------- option (a)
import grid_game_template as game  # noqa: E402  (change to your file name)

TINY = """
#####
#H.*#
#####
"""


def test_grid_reads_the_level():
    grid = game.Grid(TINY)
    assert (grid.rows, grid.cols) == (3, 5)
    assert grid.find("H") == (1, 1)
    assert grid.count("*") == 1


def test_hero_cannot_walk_through_walls():
    grid = game.Grid(TINY)
    hero = game.Hero(1, 1)
    assert hero.move(grid, -1, 0) is False, "There is a wall above the hero."
    assert (hero.row, hero.col) == (1, 1)


def test_hero_collects_treasure():
    grid = game.Grid(TINY)
    hero = game.Hero(1, 1)
    hero.move(grid, 0, 1)
    hero.move(grid, 0, 1)
    assert hero.treasure == 1 and grid.count("*") == 0


# ---------------------------------------------------------------- option (b)
import art_app_template as art  # noqa: E402


def test_gallery_save_and_load_round_trip(tmp_path):
    gallery = art.Gallery()
    gallery.add(art.Square(10, 20, 30, "#0072B2"))
    gallery.add(art.Shape(-5, 0, 12, "#E69F00"))
    gallery.save(tmp_path / "art.json")
    copy = art.Gallery()
    assert copy.load(tmp_path / "art.json")
    saved = [s.to_dict() for s in gallery.shapes]
    assert [s.to_dict() for s in copy.shapes] == saved
    assert isinstance(copy.shapes[0], art.Square), \
        "Loading should rebuild the right class."


# ---------------------------------------------------------------- option (c)
import data_app_template as data_app  # noqa: E402


def test_cleaning_skips_empty_rows_and_tidies_text():
    data = data_app.load_dataset(data_app.DATA_FILE)
    assert len(data.rows) == 13, "The empty row should be skipped."
    assert data.count_by("genre")["action"] == 5, \
        "' Action ' should be cleaned to 'action'."


def test_average_ignores_blanks():
    data = data_app.DataSet([{"rating": 4}, {"rating": None}, {"rating": 2}])
    assert data.average("rating") == 3
