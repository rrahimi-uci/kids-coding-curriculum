# Palette Stripes
# Make a list of colors, then draw one stripe for each color.

import turtle


def build_palette():
    """Return a list of color-blind-safe (Okabe-Ito) colors."""
    palette = ["#E69F00", "#56B4E9", "#009E73"]   # orange, sky blue, green
    # TODO 1: append blue "#0072B2" and vermillion "#D55E00" to the list.
    # TODO 2 (extra): append reddish purple "#CC79A7" too.
    return palette


def draw_stripe(t, x, y, width, height, color, label):
    """Draw one filled stripe with its top-left corner at (x, y) and a label under it."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    for side in [width, height, width, height]:
        t.forward(side)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(x + width / 2, y - height - 25)
    t.write(label, align="center", font=("Arial", 14, "bold"))


def draw_stripes(t, colors, width=60):
    """Draw one stripe for every color in the list, left to right."""
    x = -len(colors) * width / 2          # start far enough left to center the stripes
    # TODO 3: this only draws stripe number 0. Use a loop:
    #   for i in range(len(colors)):
    # then draw stripe i (label str(i)) and move x along by width.
    draw_stripe(t, x, 100, width, 200, colors[0], "0")


if __name__ == "__main__":
    palette = build_palette()
    print(f"My palette has {len(palette)} colors.")
    # TODO 4: print the first color (index 0) and the last color (index -1).
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    draw_stripes(t, palette)
    turtle.done()
