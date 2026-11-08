"""My Art App - starter template for project option (b).

This already works: press Run, click to add shapes, press S to save your
picture and L to load it again. Your job is to make it YOURS: new shape
classes, a recursive pattern, your own palette. Look for the TODO comments.

Before you start, rename this file to a name nobody else uses,
for example spiral_studio.py, and change the import in test_my_project.py.
"""

import json
import random
import turtle
from pathlib import Path

SAVE_FILE = Path(__file__).resolve().parent / "my_art.json"

# Okabe-Ito color-blind-safe palette
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]


class Shape:
    """Base class: every shape has a kind, a position, a size and a color."""

    kind = "dot"

    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, pen):
        pen.goto(self.x, self.y)
        pen.dot(self.size, self.color)

    def to_dict(self):
        """Turn the shape into a dictionary so json can save it."""
        return {"kind": self.kind, "x": self.x, "y": self.y,
                "size": self.size, "color": self.color}


class Square(Shape):
    """A Square IS a Shape (inheritance). It only changes how it draws."""

    kind = "square"

    def draw(self, pen):
        pen.goto(self.x - self.size / 2, self.y - self.size / 2)
        pen.color(self.color)
        pen.pendown()
        pen.begin_fill()
        for _ in range(4):
            pen.forward(self.size)
            pen.left(90)
        pen.end_fill()
        pen.penup()


# TODO: add your own shape class, e.g. class Star(Shape).
# TODO (algorithm): add a RECURSIVE shape, e.g. a fractal tree or a spiral:
#     def draw(self, pen): ... calls a helper that calls itself with a
#     smaller size, and STOPS at a base case (size < 5).

SHAPE_CLASSES = {"dot": Shape, "square": Square}  # TODO: add your classes here


def shape_from_dict(data):
    """The opposite of to_dict: build the right kind of shape again."""
    shape_class = SHAPE_CLASSES[data["kind"]]
    return shape_class(data["x"], data["y"], data["size"], data["color"])


class Gallery:
    """A Gallery HAS a list of shapes (composition)."""

    def __init__(self):
        self.shapes = []

    def add(self, shape):
        self.shapes.append(shape)

    def draw_all(self, pen):
        pen.clear()
        for shape in self.shapes:
            shape.draw(pen)  # each shape draws itself its own way

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            data = [shape.to_dict() for shape in self.shapes]
            json.dump(data, file, indent=1)

    def load(self, filename):
        """Replace the shapes with the ones in the file (if it exists)."""
        if not Path(filename).exists():
            return False
        with open(filename, encoding="utf-8") as file:
            self.shapes = [shape_from_dict(data) for data in json.load(file)]
        return True


def main():
    gallery = Gallery()
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    screen = turtle.Screen()
    screen.title("My Art App - click to add, S to save, L to load")
    screen.tracer(0)

    def add_shape(x, y):
        shape_class = random.choice(list(SHAPE_CLASSES.values()))
        size = random.randint(10, 60)
        gallery.add(shape_class(x, y, size, random.choice(PALETTE)))
        gallery.draw_all(pen)
        screen.update()

    def save():
        gallery.save(SAVE_FILE)

    def load():
        gallery.load(SAVE_FILE)
        gallery.draw_all(pen)
        screen.update()

    screen.onclick(add_shape)
    screen.onkey(save, "s")
    screen.onkey(load, "l")
    screen.listen()
    add_shape(0, 0)  # start with one shape so the window is not empty


if __name__ == "__main__":
    main()
    turtle.done()
