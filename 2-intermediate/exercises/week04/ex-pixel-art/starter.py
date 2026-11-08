# Pixel Art
# The picture is a list of strings: one string per row, one letter per pixel.

import turtle

# K = black, O = orange, Y = yellow, B = blue, S = sky blue,
# G = green, R = vermillion, P = purple, . = empty
INVADER = [
    "..G.....G..",
    "...G...G...",
    "..GGGGGGG..",
    ".GGKGGGKGG.",
    "GGGGGGGGGGG",
    "G.GGGGGGG.G",
    "G.G.....G.G",
    "...GG.GG...",
]


def color_for(pixel):
    """Return the color code for one letter of the picture."""
    if pixel == "K":
        return "#000000"
    elif pixel == "O":
        return "#E69F00"
    elif pixel == "Y":
        return "#F0E442"
    elif pixel == "B":
        return "#0072B2"
    elif pixel == "S":
        return "#56B4E9"
    elif pixel == "G":
        return "#009E73"
    elif pixel == "R":
        return "#D55E00"
    elif pixel == "P":
        return "#CC79A7"
    else:
        return "white"


def count_pixels(grid, letter):
    """Return how many times a letter appears in the whole grid."""
    count = 0
    # TODO 2: a loop inside a loop: for row in grid:  then  for pixel in row:
    # add 1 to count when the pixel is the letter.
    return count


def draw_square(t, x, y, size, color):
    """Draw one filled square with its top-left corner at (x, y)."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()


def draw_grid(t, grid, size):
    """Draw every pixel that is not '.', row by row, from the top."""
    y = len(grid) * size / 2
    # TODO 1: this only draws the FIRST row (grid[0]).
    # Wrap the lines below in an outer loop:  for row in grid:
    # and after each row move down:  y = y - size
    row = grid[0]
    x = -len(row) * size / 2
    for pixel in row:
        if pixel != ".":
            draw_square(t, x, y, size, color_for(pixel))
        x = x + size


if __name__ == "__main__":
    print(f"Green pixels: {count_pixels(INVADER, 'G')}")
    turtle.tracer(0)                       # draw everything at once (fast)
    t = turtle.Turtle()
    t.hideturtle()
    draw_grid(t, INVADER, 30)
    turtle.update()
    turtle.done()
