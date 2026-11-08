# Treasure map - reference solution
# A game map stored as a GRID (a list of lists).
#   ~ water   ^ mountain   . grass   T treasure   S start
# Each tile is drawn with a color AND its own letter.

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
        total += row.count(tile)
    return total


def neighbors(grid, row, col):
    """The (row, col) of the cells directly up, down, left and right,
    leaving out any that would be off the edge of the map."""
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc
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
