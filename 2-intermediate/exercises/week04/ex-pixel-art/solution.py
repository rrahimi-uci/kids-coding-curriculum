# Pixel Art - reference solution
# The picture is a list of strings: one string per row, one letter per
# pixel. A loop inside a loop (a nested loop) visits every pixel:
# the outer loop goes down the rows, the inner loop goes along each row.

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
    for row in grid:
        for pixel in row:
            if pixel == letter:
                count = count + 1
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
    for row in grid:                       # outer loop: one row at a time
        x = -len(row) * size / 2
        for pixel in row:                  # inner loop: one pixel at a time
            if pixel != ".":
                draw_square(t, x, y, size, color_for(pixel))
            x = x + size
        y = y - size                       # next row is lower down


if __name__ == "__main__":
    print(f"Green pixels: {count_pixels(INVADER, 'G')}")
    turtle.tracer(0)                       # draw everything at once (fast)
    t = turtle.Turtle()
    t.hideturtle()
    draw_grid(t, INVADER, 30)
    turtle.update()
    turtle.done()
