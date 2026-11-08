# Koch snowflake - reference solution
# A Koch line of depth 0 is a straight line.
# A Koch line of depth n is FOUR Koch lines of depth n-1, each a third as long,
# with a bump in the middle:   ___/\___
# Three Koch lines in a triangle make a snowflake.

import turtle

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]


def koch(t, length, depth):
    """Draw one Koch line."""
    if depth == 0:                 # base case: just a straight line
        t.forward(length)
        return
    third = length / 3
    koch(t, third, depth - 1)      # first third
    t.left(60)
    koch(t, third, depth - 1)      # up the bump
    t.right(120)
    koch(t, third, depth - 1)      # down the bump
    t.left(60)
    koch(t, third, depth - 1)      # last third


def snowflake(t, length, depth):
    """Three Koch lines, turning 120 degrees after each, make a snowflake."""
    for _ in range(3):
        koch(t, length, depth)
        t.right(120)


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Koch snowflakes")
    screen.tracer(0)
    t = turtle.Turtle()
    t.hideturtle()
    for depth, x in [(0, -300), (1, -100), (3, 100)]:
        t.penup()
        t.goto(x, 60)
        t.setheading(0)
        t.pendown()
        t.pencolor(PALETTE[depth + 4])
        t.pensize(2)
        snowflake(t, 160, depth)
        t.penup()
        t.goto(x + 80, -170)
        t.pencolor("black")
        t.write(f"depth {depth}", align="center", font=("Arial", 14, "normal"))
    screen.update()
    turtle.done()
