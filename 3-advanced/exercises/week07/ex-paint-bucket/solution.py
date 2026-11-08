# Paint bucket - reference solution
# The picture is a GRID: a list of rows, and each row is a list of cells.
#   grid[row][col] is one cell. Row 0 is the top, col 0 is the left.
# Click a cell to pour paint into it. The paint spreads to every touching
# cell of the same color - that is FLOOD FILL, and it uses recursion.
# Keys 1-5 choose the paint. Every color also has its own letter.

import turtle

# Each symbol has a color (Okabe-Ito palette) AND a letter, so you never
# need to tell colors apart to use the program.
COLORS = {
    ".": "white",      # empty paper
    "#": "#000000",    # black walls
    "O": "#E69F00",    # orange
    "S": "#56B4E9",    # sky blue
    "G": "#009E73",    # green
    "Y": "#F0E442",    # yellow
    "P": "#CC79A7",    # purple
}
PAINT_KEYS = {"1": "O", "2": "S", "3": "G", "4": "Y", "5": "P"}

PICTURE = [
    "..............",
    "..######......",
    "..#....#......",
    "..#....#..###.",
    "..######..#.#.",
    "..........###.",
    "....#####.....",
    "....#...#.....",
    "....#...#.....",
    "....#####.....",
]

CELL = 34          # size of one cell on screen, in pixels


def make_grid(rows):
    """Turn a list of strings into a grid (a list of lists of letters)."""
    return [list(row) for row in rows]


def count_tiles(grid, symbol):
    """How many cells in the grid hold this symbol?"""
    total = 0
    for row in grid:
        for cell in row:
            if cell == symbol:
                total += 1
    return total


def flood_fill(grid, row, col, old, new):
    """Paint the cell at (row, col) and every touching old cell with new."""
    # Base case 1: we walked off the edge of the grid.
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return
    # Base case 2: this cell is not the color we are replacing
    # (a wall, or a cell we already painted).
    if grid[row][col] != old:
        return
    grid[row][col] = new
    # Recursive case: spread up, down, left and right.
    flood_fill(grid, row - 1, col, old, new)
    flood_fill(grid, row + 1, col, old, new)
    flood_fill(grid, row, col - 1, old, new)
    flood_fill(grid, row, col + 1, old, new)


def paint(grid, row, col, new):
    """Pour new paint into the cell at (row, col)."""
    old = grid[row][col]
    if old == new or old == "#":    # same color or a wall: nothing to do
        return
    flood_fill(grid, row, col, old, new)


# ---------------------------------------------------------------- drawing
def cell_corner(grid, row, col):
    """Screen position of the top-left corner of a cell (grid is centered)."""
    left = -len(grid[0]) * CELL / 2
    top = len(grid) * CELL / 2
    return left + col * CELL, top - row * CELL


def cell_at(grid, x, y):
    """Which (row, col) is under the screen point (x, y)? None if outside."""
    left, top = cell_corner(grid, 0, 0)
    col = int((x - left) // CELL)
    row = int((top - y) // CELL)
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return row, col
    return None


def draw_grid(t, grid):
    t.clear()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            symbol = grid[row][col]
            x, y = cell_corner(grid, row, col)
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.pencolor("#555555")
            t.fillcolor(COLORS[symbol])
            t.begin_fill()
            for _ in range(4):
                t.forward(CELL)
                t.right(90)
            t.end_fill()
            if symbol not in ".#":          # write the letter too
                t.penup()
                t.goto(x + CELL / 2, y - CELL + 8)
                t.pencolor("black")
                t.write(symbol, align="center", font=("Arial", 12, "bold"))


def main():
    screen = turtle.Screen()
    screen.title("Paint bucket: click to fill, keys 1-5 change paint")
    screen.tracer(0)
    grid = make_grid(PICTURE)
    pen = turtle.Turtle()
    pen.hideturtle()
    state = {"paint": "O"}

    def redraw():
        draw_grid(pen, grid)
        pen.penup()
        pen.goto(0, -len(grid) * CELL / 2 - 30)
        pen.pencolor("black")
        pen.write(f"Paint: {state['paint']}   (keys: 1=O 2=S 3=G 4=Y 5=P)",
                  align="center", font=("Arial", 14, "normal"))
        screen.update()

    def on_click(x, y):
        spot = cell_at(grid, x, y)
        if spot is not None:
            paint(grid, spot[0], spot[1], state["paint"])
            redraw()

    def chooser(symbol):
        def choose():
            state["paint"] = symbol
            redraw()
        return choose

    for key, symbol in PAINT_KEYS.items():
        screen.onkey(chooser(symbol), key)
    screen.onscreenclick(on_click)
    screen.listen()
    redraw()
    turtle.done()


if __name__ == "__main__":
    main()
