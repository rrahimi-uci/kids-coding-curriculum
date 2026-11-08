# TEACHER REFERENCE SOLUTION: Exercise 7.3 - Paint bucket (flood fill)
#
# What the program does: shows a small picture made of squares. Click a
# square and the chosen paint spreads to every touching square of the same
# color, like the paint-bucket tool in a drawing app. Walls stop the paint.
# Key ideas: a grid (a list of rows, each row a list of cells), nested
# loops, and recursion with TWO base cases.
# Approach: flood_fill paints one cell, then asks itself to do the same job
# for the cell above, below, left and right. It stops (base case) when it
# is off the grid or the cell is not the old color. Because each painted
# cell is no longer the old color, the paint never goes back and forth.
#
# Coordinates: grid[row][col]. Row 0 is the TOP, col 0 is the LEFT.
# Only the three TODO functions below are the child's job; the drawing code
# further down is given to the child ready-made.

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
    for row in grid:            # the outer loop visits each row...
        for cell in row:        # ...the inner loop visits each cell in it
            if cell == symbol:
                total += 1
    return total


def flood_fill(grid, row, col, old, new):
    """Paint the cell at (row, col) and every touching old cell with new."""
    # Base case 1: we walked off the edge of the grid. This check MUST come
    # first, otherwise grid[row][col] below could crash (or, with a negative
    # index, quietly read from the opposite edge).
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return
    # Base case 2: this cell is not the color we are replacing
    # (a wall, or a cell we already painted).
    if grid[row][col] != old:
        return
    # Paint BEFORE spreading. Once painted, this cell no longer equals old,
    # so neighbors that spread back here stop at base case 2 instead of
    # bouncing between cells forever.
    grid[row][col] = new
    # Recursive case: spread up, down, left and right.
    flood_fill(grid, row - 1, col, old, new)
    flood_fill(grid, row + 1, col, old, new)
    flood_fill(grid, row, col - 1, old, new)
    flood_fill(grid, row, col + 1, old, new)


def paint(grid, row, col, new):
    """Pour new paint into the cell at (row, col)."""
    old = grid[row][col]
    # Painting a color with itself would never make cells "different", so
    # the fill would loop forever; and walls are never painted.
    if old == new or old == "#":
        return
    flood_fill(grid, row, col, old, new)


# ---------------------------------------- drawing
# Everything below is given code that shows the grid on screen and turns
# mouse clicks into grid positions. It is not part of the exercise.
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


# Common mistakes children make here:
#   - Forgetting base case 2 (the "!= old" check): the paint then floods
#     through the walls and the program ends in a RecursionError.
#   - Painting the cell AFTER the four recursive calls, or never painting
#     it, so cells are visited again and again without end.
#   - Mixing up row and col, for example flood_fill(grid, col, row, ...),
#     or counting with len(grid) for the width instead of len(grid[0]).
#
# Another correct way for count_tiles: let each row count for us.
#   return sum(row.count(symbol) for row in grid)
