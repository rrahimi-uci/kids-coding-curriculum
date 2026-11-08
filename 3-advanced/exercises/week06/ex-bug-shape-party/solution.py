# TEACHER REFERENCE SOLUTION: Bug Hunt 4 - Shape Party (inheritance bugs)
#
# What the program does: draws a row of 7 colorful shapes, alternating
# 4 hexagons (top row) and 3 diamonds (bottom row).
# Key ideas: inheritance (Hexagon and Diamond are kinds of Shape), calling
# the parent's __init__ with super(), overriding a method, and calling a
# method with ().
# Approach: Shape holds what every shape shares (position, size, color and
# how to get the pen ready). Each child class overrides draw() to draw its
# own outline. draw_party simply asks every shape to draw itself.
#
# The three bugs (marked FIX below):
#   FIX 1: Hexagon.__init__ forgot super().__init__(x, y, size, color)
#   FIX 2: Diamond had "def drow" (typo), so it never replaced Shape.draw
#   FIX 3: draw_party wrote "shape.draw" without (), so nothing was drawn

import turtle

# Colors chosen so that people with color-blindness can still tell them apart.
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7"]


class Shape:
    """The parent class: what every shape has in common."""

    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def start(self, t):
        """Move the pen to the shape's spot, facing right, with its colors."""
        t.penup()  # lift the pen so travelling does not leave a line
        t.goto(self.x, self.y)
        t.setheading(0)
        t.pendown()
        t.color("black", self.color)  # black outline, shape's own fill color

    def draw(self, t):
        # A plain Shape is just a dot. The children below replace this.
        self.start(t)
        t.dot(self.size, self.color)


class Hexagon(Shape):
    def __init__(self, x, y, size, color, label="hex"):
        # FIX 1: the child must ask the parent to set up x, y, size and
        # color. Without this line a Hexagon had no color and crashed later.
        super().__init__(x, y, size, color)
        self.label = label  # the only thing a Hexagon adds by itself

    def draw(self, t):
        self.start(t)
        t.begin_fill()
        for _ in range(6):
            t.forward(self.size)
            t.left(60)  # 6 turns of 60 degrees make a full circle (360)
        t.end_fill()


class Diamond(Shape):
    # FIX 2: the name must be exactly "draw" to override the parent's draw.
    # "drow" is just a new, unused method, so Python kept drawing a dot.
    def draw(self, t):
        self.start(t)
        t.left(45)  # tilt a square by 45 degrees so it stands on a corner
        t.begin_fill()
        for _ in range(4):
            t.forward(self.size)
            t.left(90)
        t.end_fill()


def draw_party(shapes, t):
    for shape in shapes:
        # FIX 3: the () are what actually RUNS the method. Without them
        # Python only looks at the method and moves on, with no error.
        shape.draw(t)


def make_party():
    shapes = []
    for i in range(7):
        x = -330 + i * 100  # spread the 7 shapes across the window
        if i % 2 == 0:
            shapes.append(Hexagon(x, 40, 40, PALETTE[i]))
        else:
            # +30 nudges each diamond so it sits under the gap between hexagons
            shapes.append(Diamond(x + 30, -80, 55, PALETTE[i]))
    return shapes


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Shape Party")
    screen.tracer(0)  # draw everything off-screen first, then show it at once
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pensize(2)
    draw_party(make_party(), pen)
    screen.update()
    turtle.done()


# Common mistakes children make here:
#   - Fixing the typo "drow" but also leaving the missing () in draw_party,
#     so the window stays empty and they think the first fix did nothing.
#   - Writing super().__init__() with no arguments, or forgetting
#     "self.label = label" after it (then label is lost).
#   - Writing super.__init__(...) without the () after super.
#
# Another correct way: pass the pen-setup through a shared helper, as
# Shape.start already does, instead of copying those lines into each draw().
