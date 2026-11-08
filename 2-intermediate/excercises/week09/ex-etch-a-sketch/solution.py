# Etch-a-Sketch - reference solution
# Event-driven: the program sets up "handlers" (functions) and then WAITS.
# When a key is pressed, turtle calls the matching handler for us.
#   screen.onkey(go_up, "Up")   means "when Up is pressed, call go_up"
#   (no brackets after go_up: we hand over the function, we do not call it)

import turtle

STEP = 10
COLOURS = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#000000"]
HELP = "Arrows: draw   space: pen up/down   n: next colour   c: shake clean"

settings = {"colour": 0}   # which colour from the list we are using


def go_up():
    pen.setheading(90)
    pen.forward(STEP)


def go_down():
    pen.setheading(270)
    pen.forward(STEP)


def go_left():
    pen.setheading(180)
    pen.forward(STEP)


def go_right():
    pen.setheading(0)
    pen.forward(STEP)


def pen_up_or_down():
    """Space bar: lift the pen if it is down, put it down if it is up."""
    if pen.isdown():
        pen.penup()
        pen.shape("arrow")    # the shape shows the pen is up (not colour alone)
    else:
        pen.pendown()
        pen.shape("turtle")


def next_colour():
    """n: move to the next colour in the list (back to the first after the last)."""
    settings["colour"] = (settings["colour"] + 1) % len(COLOURS)
    pen.pencolor(COLOURS[settings["colour"]])


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
    pen.pencolor(COLOURS[0])

    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    screen.onkey(pen_up_or_down, "space")
    screen.onkey(next_colour, "n")
    screen.onkey(shake_clean, "c")
    screen.listen()        # start listening for key presses
    turtle.done()          # wait for events until the window is closed
