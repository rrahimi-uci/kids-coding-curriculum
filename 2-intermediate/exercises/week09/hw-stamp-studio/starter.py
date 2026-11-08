# Stamp Studio
# Move the turtle with the arrow keys and press s to stamp a copy of it.
# p picks the next shape, n picks the next color, c clears all stamps.
# The current shape and color are kept in a dictionary called studio.
# Do the TODOs in order. Press Run, then CLICK the window so it hears keys.

import turtle

STEP = 30
SHAPES = ["turtle", "circle", "square", "triangle"]
COLORS = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]
HELP = "Arrows: move   s: stamp   p: next shape   n: next color   c: clear"

studio = {"shape": 0, "color": 0}


def next_index(index, length):
    """The next position in a list of this length, back to 0 after the last."""
    # TODO 1: return index + 1, but go back to 0 after the last one.
    #         Hint: (index + 1) % length   (% gives the remainder)
    return index


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


# TODO 2: write next_color(), like next_shape(), using studio["color"],
#         COLORS and stamper.color(...)


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
    stamper.penup()
    stamper.shapesize(2)
    stamper.shape(SHAPES[studio["shape"]])
    stamper.color(COLORS[studio["color"]])

    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    screen.onkey(stamp_here, "s")
    # TODO 3: connect "p" to next_shape and "n" to next_color
    screen.onkey(clear_all, "c")
    screen.listen()
    turtle.done()
