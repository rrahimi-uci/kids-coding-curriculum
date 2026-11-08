# TEACHER REFERENCE SOLUTION: Homework 9 - Stamp Studio
#
# What it does: an art program played with the keyboard. Arrows move the
# turtle, s stamps a copy of it, p picks the next shape, n picks the next
# color and c clears all the stamps.
# Key ideas: event-driven programming (keys call our functions), keeping
# state in a dictionary, and going around a list with the remainder operator %.
# Approach: next_index() gives the next position in a list and wraps back to
# 0 after the last one. next_shape() and next_color() both use it, so they
# are twins. Then p and n are connected to them with screen.onkey().

import turtle

STEP = 30
SHAPES = ["turtle", "circle", "square", "triangle"]
COLORS = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
          "#0072B2", "#D55E00", "#CC79A7", "#000000"]
HELP = "Arrows: move   s: stamp   p: next shape   n: next color   c: clear"

studio = {"shape": 0, "color": 0}   # positions in SHAPES and COLORS right now


def next_index(index, length):
    """The next position in a list of this length, back to 0 after the last."""
    # % gives the remainder after dividing. With length 4: 3 + 1 = 4, and the
    # remainder of 4 / 4 is 0, so after the last position we go back to 0.
    # For the other positions the remainder is just index + 1.
    return (index + 1) % length


def move(dx, dy):
    stamper.goto(stamper.xcor() + dx, stamper.ycor() + dy)


def go_up():
    move(0, STEP)


def go_down():
    move(0, -STEP)


def go_left():
    move(-STEP, 0)


def go_right():
    move(STEP, 0)


def stamp_here():
    stamper.stamp()


def next_shape():
    studio["shape"] = next_index(studio["shape"], len(SHAPES))
    stamper.shape(SHAPES[studio["shape"]])


def next_color():
    # Same pattern as next_shape(), but with the color position and list.
    studio["color"] = next_index(studio["color"], len(COLORS))
    stamper.color(COLORS[studio["color"]])


def clear_all():
    stamper.clearstamps()


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Stamp Studio")

    helper = turtle.Turtle()
    helper.hideturtle()
    helper.penup()
    helper.goto(0, 260)
    helper.write(HELP, align="center", font=("Arial", 14, "normal"))

    stamper = turtle.Turtle()
    stamper.penup()                  # moving should not draw lines, only stamps
    stamper.shapesize(2)
    stamper.shape(SHAPES[studio["shape"]])
    stamper.color(COLORS[studio["color"]])

    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    screen.onkey(stamp_here, "s")
    # Hand over the functions themselves: no parentheses after the names.
    screen.onkey(next_shape, "p")
    screen.onkey(next_color, "n")
    screen.onkey(clear_all, "c")
    screen.listen()                  # without this the window ignores the keyboard
    turtle.done()


# Common mistakes children make here:
# - Writing screen.onkey(next_shape(), "p") with parentheses. That runs the
#   function once straight away instead of waiting for the key.
# - Returning index + 1 without the %: after the last shape the next press
#   crashes with an IndexError instead of going back to the first one.
# - In next_color(), copying next_shape() but leaving studio["shape"] or
#   SHAPES in it, so n changes the shape instead of the color.
# - Using % with the wrong number, e.g. (index + 1) % 3 instead of
#   % length: some shapes or colors are never reached.
#
# Another correct way: with an if instead of %:
#     index = index + 1
#     if index == length:
#         index = 0
#     return index
