# TEACHER REFERENCE SOLUTION: Palette Stripes (Exercise 3.1)
#
# What the program does: it builds a list of color-blind-safe colors and draws
# one tall stripe for each, left to right, with its index number written under it.
# Key ideas practiced: lists, append(), len(), index numbers starting at 0, and
# looping over a list with "for i in range(len(colors))".
# Approach: build_palette() makes the list. draw_stripes() loops once for each
# color, draws that stripe, and then moves the starting spot one stripe to the
# right so the stripes sit side by side instead of on top of each other.
# Every stripe is labeled with its index number, so the picture never relies on
# color alone to be understood.

import turtle


def build_palette():
    """Return a list of color-blind-safe (Okabe-Ito) colors."""
    palette = ["#E69F00", "#56B4E9", "#009E73"]   # orange, sky blue, green
    palette.append("#0072B2")                     # blue
    palette.append("#D55E00")                     # vermillion
    palette.append("#CC79A7")                     # reddish purple (the extra TODO 2)
    return palette


def draw_stripe(t, x, y, width, height, color, label):
    """Draw one filled stripe with its top-left corner at (x, y) and a label under it."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    # A rectangle: across, down, across, down (turning right each time).
    for side in [width, height, width, height]:
        t.forward(side)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(x + width / 2, y - height - 25)    # the middle of the stripe, just below it
    t.write(label, align="center", font=("Arial", 14, "bold"))


def draw_stripes(t, colors, width=60):
    """Draw one stripe for every color in the list, left to right."""
    x = -len(colors) * width / 2          # start far enough left to center the stripes
    for i in range(len(colors)):          # i counts 0, 1, 2, ... one number per color
        draw_stripe(t, x, 100, width, 200, colors[i], str(i))   # str() turns 3 into "3"
        x = x + width                     # slide right so the next stripe does not overlap


if __name__ == "__main__":
    palette = build_palette()
    print(f"My palette has {len(palette)} colors.")
    # Index 0 is the first item. Index -1 counts from the end, so it is the last.
    print(f"The first color is {palette[0]} and the last is {palette[-1]}.")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    draw_stripes(t, palette)
    turtle.done()


# Common mistakes children make here:
# - Forgetting to add width to x inside the loop, so every stripe is drawn in
#   the same place and only the last one can be seen.
# - Passing the number i to draw_stripe instead of the color colors[i] (or
#   forgetting str(i) for the label, which must be text).
# - Using range(1, len(colors)), which skips stripe number 0.
# - Writing palette.append = "#0072B2" with an equals sign instead of brackets.
#
# Another correct way: loop over the colors directly and count with enumerate.
#   for i, color in enumerate(colors):
#       draw_stripe(t, x, 100, width, 200, color, str(i))
#       x = x + width
