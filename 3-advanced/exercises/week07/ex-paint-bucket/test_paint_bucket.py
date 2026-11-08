"""Checks for Exercise 7.3 - Paint bucket (flood fill)."""

BOX = [
    "......",
    ".###..",
    ".#.#..",
    ".###..",
    "......",
]


def test_count_tiles(load_target):
    program = load_target()
    grid = program.make_grid(BOX)
    assert program.count_tiles(grid, "#") == 8, "The test box has 8 wall cells '#'. count_tiles should find all 8."
    assert program.count_tiles(grid, ".") == 22, "The test box has 22 empty cells '.'."
    assert program.count_tiles(grid, "O") == 0, "There is no 'O' in the test box, so the count should be 0."


def test_fill_spreads_to_every_touching_cell(load_target):
    program = load_target()
    grid = program.make_grid(BOX)
    program.flood_fill(grid, 0, 0, ".", "S")
    count = program.count_tiles(grid, "S")
    assert count == 21, (f"Filling the outside of the box should paint 21 cells, but {count} were painted. "
                         "Does your fill spread up, down, left AND right?")


def test_fill_stops_at_walls(load_target):
    program = load_target()
    grid = program.make_grid(BOX)
    program.flood_fill(grid, 0, 0, ".", "S")
    assert grid[2][2] == ".", "The paint leaked through the wall into the middle of the box!"
    assert program.count_tiles(grid, "#") == 8, "The walls should never be painted."


def test_fill_inside_a_shape(load_target):
    program = load_target()
    grid = program.make_grid(BOX)
    program.paint(grid, 2, 2, "G")
    assert grid[2][2] == "G", "The cell you clicked should be painted."
    assert program.count_tiles(grid, "G") == 1, "Only the one cell inside the box should be painted."


def test_painting_the_same_color_twice_is_safe(load_target):
    program = load_target()
    grid = program.make_grid(BOX)
    program.paint(grid, 0, 0, "P")
    program.paint(grid, 0, 0, "P")      # must not loop forever
    assert program.count_tiles(grid, "P") == 21, "Painting the same area twice should leave it the same."
