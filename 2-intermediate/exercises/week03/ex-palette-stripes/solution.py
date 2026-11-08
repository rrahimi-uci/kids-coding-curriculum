# Palette Stripes - reference solution
# A list keeps many colors in order. We add colors with append(), count
# them with len() and draw one stripe for each color with a for loop.
# Every stripe is labeled with its index number, so the picture never
# relies on color alone.

import turtle


def build_palette():
    """Return a list of color-blind-safe (Okabe-Ito) colors."""
    palette = ["#E69F00", "#56B4E9", "#009E73"]   # orange, sky blue, green
    palette.append("#0072B2")                     # blue
    palette.append("#D55E00")                     # vermillion
    palette.append("#CC79A7")                     # reddish purple
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
    for i in range(len(colors)):
        draw_stripe(t, x, 100, width, 200, colors[i], str(i))
        x = x + width


if __name__ == "__main__":
    palette = build_palette()
    print(f"My palette has {len(palette)} colors.")
    print(f"The first color is {palette[0]} and the last is {palette[-1]}.")
    for color in palette:
        print(color)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    draw_stripes(t, palette)
    turtle.done()
