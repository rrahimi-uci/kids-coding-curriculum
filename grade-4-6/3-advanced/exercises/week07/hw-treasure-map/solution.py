# TEACHER REFERENCE SOLUTION: Homework 7 - Treasure map
#
# What the program does: turns a block of text into a map, draws it in
# colored squares with a letter on each, counts the treasures, and prints
# the cells next to the start.
# Key ideas: a grid (list of lists), counting items, and "bounds checking":
# never look at a cell that is off the edge of the map.
# Approach: count_tiles asks each row to count the tile for us and adds the
# answers up. neighbors tries the four directions (up, down, left, right)
# as small steps and keeps only the cells that are really on the map.
#
# Coordinates: (row, col). Row 0 is the TOP of the map, col 0 is the LEFT.

import turtle

MAP_TEXT = """
~~~~~~~~~~~~
~~....^^..~~
~..S..^^...~
~.....^..T.~
~..~~......~
~..~~...^^.~
~~......T.~~
~~~~~~~~~~~~
"""

TILE_COLORS = {"~": "#56B4E9", "^": "#E69F00", ".": "#009E73",
                "T": "#F0E442", "S": "#CC79A7"}
CELL = 40


def load_map(text):
    """Turn the map text into a grid: one list of letters per line.
    Blank lines (like the first one) are skipped."""
    grid = []
    for line in text.splitlines():
        line = line.strip()
        if line:
            grid.append(list(line))
    return grid


def count_tiles(grid, tile):
    """How many cells in the grid hold this tile?"""
    total = 0
    for row in grid:
        total += row.count(tile)  # a list can count its own items
    return total


def neighbors(grid, row, col):
    """The (row, col) of the cells directly up, down, left and right,
    leaving out any that would be off the edge of the map."""
    result = []
    # Each pair is a step: (row change, column change) for up, down, left, right.
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc
        # Keep the cell only if it is on the map. Without this check a cell on
        # the edge would give a position that is off the map, and a negative
        # number would quietly wrap around to the opposite side.
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            result.append((r, c))
    return result


def find(grid, tile):
    """The (row, col) of the first cell holding this tile, or None."""
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == tile:
                return (r, c)
    return None


def draw_map(grid):
    # Given code: draws one colored square per cell, with its letter on it.
    t = turtle.Turtle()
    t.hideturtle()
    left = -len(grid[0]) * CELL / 2
    top = len(grid) * CELL / 2
    for r, row in enumerate(grid):
        for c, tile in enumerate(row):
            x, y = left + c * CELL, top - r * CELL
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.fillcolor(TILE_COLORS.get(tile, "white"))
            t.begin_fill()
            for _ in range(4):
                t.forward(CELL)
                t.right(90)
            t.end_fill()
            t.penup()
            t.goto(x + CELL / 2, y - CELL + 10)
            t.write(tile, align="center", font=("Arial", 14, "bold"))
    t.goto(0, top + 10)
    t.write(f"Treasure on this map: {count_tiles(grid, 'T')}",
            align="center", font=("Arial", 16, "normal"))


if __name__ == "__main__":
    world = load_map(MAP_TEXT)
    start = find(world, "S")
    print("Start is at", start)
    print("Next to the start:", neighbors(world, start[0], start[1]))
    screen = turtle.Screen()
    screen.title("Treasure map")
    screen.tracer(0)
    draw_map(world)
    screen.update()
    turtle.done()


# Common mistakes children make here:
#   - Checking only "r >= 0" (or only "r < len(grid)") so one edge still
#     gives a bad neighbor or an IndexError.
#   - Using len(grid) for the column limit instead of len(grid[0]); the
#     map is wider than it is tall, so this cuts off or overshoots columns.
#   - Returning from count_tiles inside the loop, so only the first row is
#     counted.
#
# Another correct way for count_tiles: count every cell in one expression.
#   return sum(cell == tile for row in grid for cell in row)
