# Bug Hunt 4: Shape Party
# Hexagons and diamonds should dance across the screen in 7 colours.
# There are 3 bugs: one "nothing happens at all" bug, one crash, and one
# shape that comes out wrong. Find them with Run, the error message and
# the Thonny debugger.

import turtle

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7"]


class Shape:
    def __init__(self, x, y, size, colour):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour

    def start(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.setheading(0)
        t.pendown()
        t.color("black", self.colour)

    def draw(self, t):
        self.start(t)
        t.dot(self.size, self.colour)


class Hexagon(Shape):
    def __init__(self, x, y, size, colour, label="hex"):
        self.label = label

    def draw(self, t):
        self.start(t)
        t.begin_fill()
        for _ in range(6):
            t.forward(self.size)
            t.left(60)
        t.end_fill()


class Diamond(Shape):
    def drow(self, t):
        self.start(t)
        t.left(45)
        t.begin_fill()
        for _ in range(4):
            t.forward(self.size)
            t.left(90)
        t.end_fill()


def draw_party(shapes, t):
    for shape in shapes:
        shape.draw


def make_party():
    shapes = []
    for i in range(7):
        x = -330 + i * 100
        if i % 2 == 0:
            shapes.append(Hexagon(x, 40, 40, PALETTE[i]))
        else:
            shapes.append(Diamond(x + 30, -80, 55, PALETTE[i]))
    return shapes


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Shape Party")
    screen.tracer(0)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pensize(2)
    draw_party(make_party(), pen)
    screen.update()
    turtle.done()
