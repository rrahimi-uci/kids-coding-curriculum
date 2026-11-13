# Dot Art from a File
# The picture is NOT in the code: it lives in my_art.txt.
# Each line is one dot:   x,y,size,color     for example   -150,-60,40,#009E73
# Do the TODOs in order. Press Run after each one.

import turtle

ART_FILE = "my_art.txt"


def parse_line(line):
    """Turn '-150,-60,40,#009E73' into [-150, -60, 40, '#009E73']."""
    parts = line.strip().split(",")
    # TODO 1: x, y and size must be numbers. Return a list:
    #         [int(parts[0]), int(parts[1]), int(parts[2]), parts[3]]
    return parts


def load_dots(filename):
    """Return a list of dots (one [x, y, size, color] per line). Skip empty lines."""
    dots = []
    # TODO 2: open the file in "r" mode. For every line that is not empty
    #         after strip(), append parse_line(line) to dots.
    return dots


def save_dots(filename, dots):
    """Write every dot as one line 'x,y,size,color'. "w" replaces the old file."""
    # TODO 3: open the file in "w" mode. For every dot, write one line:
    #         file.write(f"{dot[0]},{dot[1]},{dot[2]},{dot[3]}\n")
    pass


def draw_dots(pen, dots):
    """Jump to each dot's place and stamp a dot of its size and color."""
    for dot in dots:
        pen.goto(dot[0], dot[1])
        pen.dot(dot[2], dot[3])


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Dot Art from a File")
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    dots = load_dots(ART_FILE)
    draw_dots(pen, dots)
    pen.goto(0, -200)
    pen.write(f"{len(dots)} dots loaded from {ART_FILE}", align="center", font=("Arial", 14, "normal"))
    turtle.done()
