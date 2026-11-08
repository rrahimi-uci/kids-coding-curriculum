# Etch-a-Sketch
# Event-driven: the program sets up "handlers" (functions) and then WAITS.
# When a key is pressed, turtle calls the matching handler for us.
#   screen.onkey(go_up, "Up")   means "when Up is pressed, call go_up"
#   (no brackets after go_up: we hand over the function, we do not call it)
# Do the TODOs in order. Press Run, then CLICK the turtle window once so it
# can hear your keys.

import turtle

STEP = 10
COLORS = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#000000"]
HELP = "Arrows: draw   space: pen up/down   n: next color   c: shake clean"

settings = {"color": 0}   # which color from the list we are using


def go_up():
    pen.setheading(90)
    pen.forward(STEP)


# TODO 2: write go_down(), go_left() and go_right() like go_up().
#         Headings: down = 270, left = 180, right = 0.


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
    settings["color"] = (settings["color"] + 1) % len(COLORS)
    pen.pencolor(COLORS[settings["color"]])


def shake_clean():
    """c: like shaking a real Etch-a-Sketch - the drawing disappears."""
    # TODO 4: clear the pen's drawing with pen.clear()
    pass


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

    screen.onkey(go_up, "Up")
    # TODO 3: connect "Down", "Left" and "Right" to your new functions,
    #         and connect "space", "n" and "c" to the functions above.

    # TODO 1: the window is not listening for keys yet! Add:
    #         screen.listen()
    turtle.done()          # wait for events until the window is closed
