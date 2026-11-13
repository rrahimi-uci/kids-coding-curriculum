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


def test_stretch_queue_fill_matches_recursive_fill(load_target):
    """Optional stretch: only checked if the student wrote flood_fill_queue."""
    program = load_target()
    queue_fill = getattr(program, "flood_fill_queue", None)
    if queue_fill is None:
        import pytest
        pytest.skip("Stretch (optional): flood_fill_queue is not written yet.")
    for start in [(0, 0), (2, 2)]:
        expected = program.make_grid(BOX)
        actual = program.make_grid(BOX)
        old = expected[start[0]][start[1]]
        program.flood_fill(expected, start[0], start[1], old, "S")
        queue_fill(actual, start[0], start[1], old, "S")
        assert actual == expected, ("flood_fill_queue should paint exactly the same cells as "
                                    "flood_fill. Do you paint a square when you add it to the queue?")
