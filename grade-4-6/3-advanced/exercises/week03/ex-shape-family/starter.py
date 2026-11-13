# Shape Family - YOUR version
# Every shape IS A Shape: it shares x, y, size, color and the start() method.
# Each child overrides draw() - so the same call, shape.draw(t), makes a
# different picture for every class (polymorphism).
# Finish the TODOs, then open check_my_work.py and press Run.

import turtle

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7"]


class Shape:
    """Parent class. A plain Shape is drawn as a dot."""

    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def start(self, t):
        """Move the turtle to this shape's corner, ready to draw."""
        t.penup()
        t.goto(self.x, self.y)
        t.setheading(0)
        t.pendown()
        t.color("black", self.color)

    def draw(self, t):
        self.start(t)
        t.dot(self.size, self.color)


class Square(Shape):
    """(Already done - use it as an example!)"""

    def draw(self, t):
        self.start(t)
        t.begin_fill()
        for _ in range(4):
            t.forward(self.size)
            t.left(90)
        t.end_fill()


class Triangle(Shape):
    # TODO 1: override draw(self, t): like Square, but 3 sides and left(120)
    pass


class Star(Shape):
    # TODO 2: override draw(self, t): 5 sides of self.size, turning right(144)
    pass


class Polygon(Shape):
    """A shape with any number of sides. It needs one extra attribute."""

    def __init__(self, x, y, size, color, sides):
        # TODO 3: call super().__init__(x, y, size, color) first
        self.sides = sides

    def draw(self, t):
        self.start(t)
        t.begin_fill()
        for _ in range(self.sides):
            t.forward(self.size)
            t.left(360 / self.sides)
        t.end_fill()


def draw_all(shapes, t):
    """Draw every shape. We do not need to know which class each one is!"""
    for shape in shapes:
        shape.draw(t)


def make_pattern():
    """Build a 4 x 3 grid of shapes, cycling through classes and colors."""
    shapes = []
    index = 0
    for row in range(3):
        for col in range(4):
            x = -300 + col * 160
            y = 120 - row * 150
            color = PALETTE[index % len(PALETTE)]
            kind = index % 4
            if kind == 0:
                shapes.append(Square(x, y, 70, color))
            elif kind == 1:
                shapes.append(Triangle(x, y, 80, color))
            elif kind == 2:
                shapes.append(Star(x, y + 50, 90, color))
            else:
                shapes.append(Polygon(x, y, 40, color, 6))
            index = index + 1
    return shapes


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Shape Family")
    screen.tracer(0)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pensize(2)
    draw_all(make_pattern(), pen)
    screen.update()
    turtle.done()
