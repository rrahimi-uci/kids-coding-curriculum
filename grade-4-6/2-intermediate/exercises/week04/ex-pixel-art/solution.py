# TEACHER REFERENCE SOLUTION: Pixel Art (Exercise 4.2)
#
# What the program does: it draws a green space invader made of colored squares,
# and prints how many green pixels the picture has (46).
# Key idea practiced: a nested loop (a loop inside a loop). The picture is a list
# of strings: one string for each row, one letter for each pixel.
# Approach: the outer loop goes down the rows. For each row, the inner loop walks
# along the letters from left to right, drawing a square for every letter that is
# not a dot. After each row we move the drawing position down by one square.
# count_pixels() visits every letter in the same two-loop way, and counts matches.

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
    # These are color-blind-safe colors. Any other letter (like ".") is white.
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
    for row in grid:                      # outer loop: each row (a string)
        for pixel in row:                 # inner loop: each letter in that row
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
    for _ in range(4):                    # a square: go forward and turn right, four times
        t.forward(size)
        t.right(90)
    t.end_fill()


def draw_grid(t, grid, size):
    """Draw every pixel that is not '.', row by row, from the top."""
    y = len(grid) * size / 2              # start half the picture height above the middle
    for row in grid:                      # outer loop: one row at a time
        # x must be reset for every row, so each row starts at the left edge again.
        x = -len(row) * size / 2
        for pixel in row:                 # inner loop: one pixel at a time
            if pixel != ".":              # a dot means "leave this spot empty"
                draw_square(t, x, y, size, color_for(pixel))
            x = x + size                  # step right, even over empty spots
        y = y - size                      # next row is lower down (y gets smaller going down)


if __name__ == "__main__":
    print(f"Green pixels: {count_pixels(INVADER, 'G')}")
    turtle.tracer(0)                      # draw everything at once (fast)
    t = turtle.Turtle()
    t.hideturtle()
    draw_grid(t, INVADER, 30)
    turtle.update()                       # show the finished picture
    turtle.done()


# Common mistakes children make here:
# - Putting y = y - size inside the inner loop, so every pixel sits on a new row
#   and the picture becomes a diagonal line. It belongs after the inner loop.
# - Putting x = -len(row) * size / 2 before the outer loop, so each row starts where
#   the last one ended and the picture slides off to the right.
# - Using y = y + size: the y axis goes UP, so adding makes the picture upside down.
# - Making rows in a new picture with different lengths, so it looks crooked.
#
# Another correct way: count with the string method count().
#   total = 0
#   for row in grid:
#       total = total + row.count(letter)
#   return total
