# TEACHER REFERENCE SOLUTION: Exercise 9.1 - Etch-a-Sketch
#
# What it does: draw with the keyboard, like the classic toy. The arrow
# keys draw, space lifts or lowers the pen, n picks the next color and c
# clears the drawing.
# Key ideas: event-driven programming. The program sets up "handlers"
# (functions) with screen.onkey(), then WAITS. When a key is pressed, turtle
# calls the matching handler for us.
# Approach: one small function per key (go_up, go_down, ...), each turning
# the pen to a heading and moving it forward. Then every function is
# connected to its key, and screen.listen() makes the window hear the keys.
#
#   screen.onkey(go_up, "Up")   means "when Up is pressed, call go_up"
#   (no parentheses after go_up: we hand over the function, we do not call it)

import turtle

STEP = 10
COLORS = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#000000"]
HELP = "Arrows: draw   space: pen up/down   n: next color   c: shake clean"

settings = {"color": 0}   # which color from the list we are using


def go_up():
    pen.setheading(90)     # 90 degrees is straight up
    pen.forward(STEP)


def go_down():
    pen.setheading(270)    # 270 degrees is straight down
    pen.forward(STEP)


def go_left():
    pen.setheading(180)    # 180 degrees is left
    pen.forward(STEP)


def go_right():
    pen.setheading(0)      # 0 degrees is right
    pen.forward(STEP)


def pen_up_or_down():
    """Space bar: lift the pen if it is down, put it down if it is up."""
    if pen.isdown():
        pen.penup()
        pen.shape("arrow")    # the shape shows the pen is up (not color alone)
    else:
        pen.pendown()
        pen.shape("turtle")


def next_color():
    """n: move to the next color in the list (back to the first after the last)."""
    # The % (remainder) sends the number back to 0 after the last color.
    settings["color"] = (settings["color"] + 1) % len(COLORS)
    pen.pencolor(COLORS[settings["color"]])


def shake_clean():
    """c: like shaking a real Etch-a-Sketch - the drawing disappears."""
    pen.clear()


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Etch-a-Sketch")

    helper = turtle.Turtle()
    helper.hideturtle()
    helper.penup()
    helper.goto(0, 260)
    helper.write(HELP, align="center", font=("Arial", 14, "normal"))

    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.pensize(3)
    pen.speed(0)
    pen.pencolor(COLORS[0])

    # Connect each key to its function (no parentheses after the names).
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    screen.onkey(pen_up_or_down, "space")
    screen.onkey(next_color, "n")
    screen.onkey(shake_clean, "c")
    screen.listen()        # without this the window ignores the keyboard
    turtle.done()          # wait for events until the window is closed


# Common mistakes children make here:
# - Writing screen.onkey(go_down(), "Down") with parentheses. That runs
#   go_down once, straight away, instead of waiting for the key.
# - Forgetting screen.listen(), or forgetting to click the window first:
#   the keys seem to do nothing.
# - Copying go_up for the other directions but leaving the heading at 90,
#   so every arrow goes up.
# - Mistyping a key name, e.g. "up" instead of "Up", or "Space" instead of
#   "space". Key names must match exactly.
#
# Another correct way: one function that takes the direction, using lambda
# to hand over a small ready-made function for each key:
#     def go(heading):
#         pen.setheading(heading)
#         pen.forward(STEP)
#     screen.onkey(lambda: go(270), "Down")
