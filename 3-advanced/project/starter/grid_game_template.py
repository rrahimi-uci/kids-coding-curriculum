"""My Grid Game - starter template for project option (a).

This already works: press Run and move the hero (H) with the arrow keys.
Your job is to turn it into YOUR game. Look for the TODO comments.

Before you start, rename this file to a name nobody else uses,
for example dragon_maze.py, and change the import in test_my_project.py.
"""

import turtle

CELL = 30  # size of one square in pixels

# A level is just text: # = wall, . = floor, H = hero, * = treasure.
# TODO: design your own level here (or load it from a file, see save_level).
LEVEL = """
##########
#H.....*.#
#.####...#
#....#.#.#
#.*..#.#.#
######...#
#*.......#
##########
"""


class Grid:
    """A 2D grid of one-letter strings: grid.cells[row][col]."""

    def __init__(self, text):
        lines = [line for line in text.strip().splitlines() if line]
        self.rows = len(lines)
        self.cols = max(len(line) for line in lines)
        # ljust pads short rows with walls so every row is the same length
        self.cells = [list(line.ljust(self.cols, "#")) for line in lines]

    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def get(self, row, col):
        return self.cells[row][col]

    def set(self, row, col, value):
        self.cells[row][col] = value

    def find(self, letter):
        """Return (row, col) of the first square holding letter, or None."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col] == letter:
                    return (row, col)
        return None

    def count(self, letter):
        return sum(row.count(letter) for row in self.cells)

    def is_open(self, row, col):
        return self.in_bounds(row, col) and self.cells[row][col] != "#"

    def neighbours(self, row, col):
        """Open squares next to (row, col): up, down, left, right."""
        result = []
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if self.is_open(row + d_row, col + d_col):
                result.append((row + d_row, col + d_col))
        return result

    def to_text(self):
        return "\n".join("".join(row) for row in self.cells)

    # TODO (saved file): add save_level(filename) and a load_level(filename)
    # function, so your levels live in .txt files next to this program.


class Hero:
    """The player. TODO: make a base class (for example Character) and let
    Hero AND a new Enemy class inherit from it (or use composition)."""

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.treasure = 0

    def move(self, grid, d_row, d_col):
        """Step one square unless a wall is in the way. True if moved."""
        new_row, new_col = self.row + d_row, self.col + d_col
        if not grid.is_open(new_row, new_col):
            return False
        grid.set(self.row, self.col, ".")
        self.row, self.col = new_row, new_col
        if grid.get(new_row, new_col) == "*":
            self.treasure += 1
        grid.set(new_row, new_col, "H")
        return True


# TODO (algorithm): add breadth-first search, flood fill or a recursive
# function. Idea: an enemy that uses BFS (with collections.deque) to chase H.


# ---------------------------------------------------------------- drawing
# Shapes AND letters, so the game never depends on colour alone.
COLOURS = {"#": "#0072B2", "*": "#E69F00", "H": "#009E73"}


def draw(pen, grid, hero):
    pen.clear()
    left = -grid.cols * CELL / 2
    top = grid.rows * CELL / 2
    for row in range(grid.rows):
        for col in range(grid.cols):
            letter = grid.get(row, col)
            x = left + col * CELL
            y = top - row * CELL
            if letter in COLOURS:
                pen.goto(x, y)
                pen.color("black", COLOURS[letter])
                pen.begin_fill()
                for _ in range(4):
                    pen.forward(CELL)
                    pen.right(90)
                pen.end_fill()
            if letter in "H*":
                pen.goto(x + CELL / 2, y - CELL + 6)
                pen.write(letter, align="center", font=("Arial", 14, "bold"))
    pen.goto(0, top + 10)
    pen.write(f"Treasure: {hero.treasure}", align="center",
              font=("Arial", 14, "bold"))
    turtle.update()


def main():
    grid = Grid(LEVEL)
    row, col = grid.find("H")
    hero = Hero(row, col)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()

    def go(d_row, d_col):
        hero.move(grid, d_row, d_col)
        draw(pen, grid, hero)

    screen = turtle.Screen()
    screen.title("My Grid Game")
    screen.tracer(0)
    screen.onkey(lambda: go(-1, 0), "Up")
    screen.onkey(lambda: go(1, 0), "Down")
    screen.onkey(lambda: go(0, -1), "Left")
    screen.onkey(lambda: go(0, 1), "Right")
    screen.listen()
    draw(pen, grid, hero)


if __name__ == "__main__":
    main()
    turtle.done()
