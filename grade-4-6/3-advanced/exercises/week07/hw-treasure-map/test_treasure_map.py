"""Checks for Homework 7 - Treasure map."""

SMALL = """
~~~~
~ST~
~.^~
"""


def test_load_map_makes_rows_of_letters(load_target):
    program = load_target()
    grid = program.load_map(SMALL)
    assert len(grid) == 3, f"The small map has 3 rows, but load_map made {len(grid)}."
    assert grid[1] == ["~", "S", "T", "~"], f"Row 1 should be ['~', 'S', 'T', '~'], not {grid[1]}."


def test_count_tiles(load_target):
    program = load_target()
    grid = program.load_map(program.MAP_TEXT)
    assert program.count_tiles(grid, "T") == 2, "The big map has 2 treasures 'T'."
    assert program.count_tiles(grid, "S") == 1, "The big map has 1 start 'S'."
    grid = program.load_map(SMALL)
    assert program.count_tiles(grid, "~") == 8, "The small test map has 8 water tiles '~'."


def test_neighbors_in_the_middle(load_target):
    program = load_target()
    grid = program.load_map(SMALL)
    got = sorted(program.neighbors(grid, 1, 1))
    assert got == [(0, 1), (1, 0), (1, 2), (2, 1)], \
        f"A cell in the middle has 4 neighbors (up, down, left, right). Got {got}."


def test_neighbors_at_the_edge(load_target):
    program = load_target()
    grid = program.load_map(SMALL)
    got = sorted(program.neighbors(grid, 0, 0))
    assert got == [(0, 1), (1, 0)], \
        f"The top-left corner only has 2 neighbors - the others are off the map. Got {got}."
    got = sorted(program.neighbors(grid, 2, 3))
    assert got == [(1, 3), (2, 2)], f"The bottom-right corner only has 2 neighbors. Got {got}."
