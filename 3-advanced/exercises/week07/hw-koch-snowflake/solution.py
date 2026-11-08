# TEACHER REFERENCE SOLUTION: Homework 7 challenge - Koch snowflake
#
# What the program does: draws three snowflakes, with depth 0 (a plain
# triangle), depth 1 and depth 3 (more and more detail).
# Key idea: a fractal made by recursion. A Koch line is built from FOUR
# smaller Koch lines, and each of those is built from four even smaller ones.
# Approach: koch() draws one straight line at depth 0. At any higher depth it
# draws four lines, each a third as long, with turns that make a bump in the
# middle (___/\___). snowflake() draws three Koch lines, turning 120 degrees
# between them, so the shape closes into a triangle-like star.
# Counting: depth n has 4**n pieces per side (1, 4, 16, 64 ...).

import turtle

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]


def koch(t, length, depth):
    """Draw one Koch line."""
    if depth == 0:                 # base case: just a straight line
        t.forward(length)
        return
    # Each of the four pieces is a third as long. Four thirds with a bump
    # still end at the same spot as one straight line of the full length,
    # because the turns (left 60, right 120, left 60) add up to zero.
    third = length / 3
    koch(t, third, depth - 1)      # first third, straight ahead
    t.left(60)                     # turn to climb the bump
    koch(t, third, depth - 1)      # up the bump
    t.right(120)                   # turn to go down the other side
    koch(t, third, depth - 1)      # down the bump
    t.left(60)                     # turn back to the original direction
    koch(t, third, depth - 1)      # last third


def snowflake(t, length, depth):
    """Three Koch lines, turning 120 degrees after each, make a snowflake."""
    for _ in range(3):
        koch(t, length, depth)
        # Turning RIGHT keeps the bumps pointing outward. (Turning left
        # would push the bumps inward.)
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


# Common mistakes children make here:
#   - Using length instead of length / 3 for the four pieces, so the line
#     becomes far too long and runs off the screen.
#   - Getting the turns wrong (for example left 60, left 120): the bump
#     looks lopsided and the line no longer ends at the right place.
#   - Calling koch with depth instead of depth - 1, which never stops.
#
# Another correct way: draw the four pieces with a loop over the turns.
#   for turn in (60, -120, 60, 0):
#       koch(t, length / 3, depth - 1)
#       t.left(turn)
