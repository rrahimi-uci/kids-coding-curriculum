"""TEACHER REFERENCE SOLUTION: Shape Family

What the program does: it draws a 4 x 3 grid of shapes (squares, triangles, stars and
hexagons) in seven colors. Each kind of shape is a different class, but the picture-drawing
loop treats them all the same.

Key ideas practiced: inheritance, overriding `draw()`, `super().__init__` for a child with
an extra attribute, turtle angles (a shape closes when the turns add up to a multiple of
360 degrees), and polymorphism.

Approach: `Shape` stores x, y, size and color and has a helper `start()` that gets the
turtle ready. Square, Triangle and Star differ only in the number of sides and the turn
angle: 4 x 90, 3 x 120 and 5 x 144 (twice around the circle, which makes the star points).
"""

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
        t.penup()  # lift the pen so the trip to the corner leaves no line
        t.goto(self.x, self.y)
        t.setheading(0)  # face right, so every shape starts the same way
        t.pendown()
        t.color("black", self.color)  # black outline, shape's own fill color

    def draw(self, t):
        self.start(t)
        t.dot(self.size, self.color)


class Square(Shape):
    def draw(self, t):
        self.start(t)
        t.begin_fill()
        for _ in range(4):
            t.forward(self.size)
            t.left(90)  # 4 x 90 = 360 degrees: the square closes
        t.end_fill()


class Triangle(Shape):
    # Step 1: the same plan as Square, with 3 sides and a bigger turn.
    def draw(self, t):
        self.start(t)
        t.begin_fill()
        for _ in range(3):
            t.forward(self.size)
            t.left(120)  # 3 x 120 = 360 degrees
        t.end_fill()


class Star(Shape):
    # Step 2: 5 lines, turning RIGHT 144 degrees each time. 5 x 144 = 720 degrees, which is
    # two full turns, so the turtle ends where it started and the lines cross into a star.
    def draw(self, t):
        self.start(t)
        t.begin_fill()
        for _ in range(5):
            t.forward(self.size)
            t.right(144)
        t.end_fill()


class Polygon(Shape):
    """A shape with any number of sides. It needs one extra attribute."""

    def __init__(self, x, y, size, color, sides):
        # Step 3: the parent sets x, y, size and color, so we only add what is new.
        super().__init__(x, y, size, color)
        self.sides = sides

    def draw(self, t):
        self.start(t)
        t.begin_fill()
        for _ in range(self.sides):
            t.forward(self.size)
            t.left(360 / self.sides)  # turn an equal share of a full circle
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
            # "%" wraps around: after the 7th color we start again at the first.
            color = PALETTE[index % len(PALETTE)]
            kind = index % 4  # 0 square, 1 triangle, 2 star, 3 hexagon
            if kind == 0:
                shapes.append(Square(x, y, 70, color))
            elif kind == 1:
                shapes.append(Triangle(x, y, 80, color))
            elif kind == 2:
                # A star hangs below its starting corner, so lift it 50 to line it up with the row.
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


# Common mistakes children make here:
# - Using `left(144)` for the star: it still draws, but mirrored and hanging the other way
#   up; a wrong angle such as 72 makes a pentagon, not a star.
# - Forgetting `self.start(t)` in draw, so the shape is drawn wherever the turtle was last.
# - Forgetting `super().__init__(...)` in Polygon, so `color` (and x, y, size) are missing.
# - Writing `for _ in range(3): ... left(90)` for the triangle: the turns must add up to 360.
#
# Another correct way: one shared helper that every regular shape uses:
#     def draw_sides(self, t, sides, turn):
#         self.start(t)
#         t.begin_fill()
#         for _ in range(sides):
#             t.forward(self.size)
#             t.left(turn)
#         t.end_fill()
