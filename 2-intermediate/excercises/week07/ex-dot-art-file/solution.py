# Dot Art from a File - reference solution
# The picture is NOT in the code: it lives in my_art.txt.
# Each line is one dot:   x,y,size,colour     for example   -150,-60,40,#009E73
# Change the file and the picture changes - no coding needed!

import turtle

ART_FILE = "my_art.txt"


def parse_line(line):
    """Turn '-150,-60,40,#009E73' into [-150, -60, 40, '#009E73']."""
    parts = line.strip().split(",")
    return [int(parts[0]), int(parts[1]), int(parts[2]), parts[3]]


def load_dots(filename):
    """Return a list of dots (one [x, y, size, colour] per line). Skip empty lines."""
    dots = []
    with open(filename, "r") as file:
        for line in file:
            if line.strip() != "":
                dots.append(parse_line(line))
    return dots


def save_dots(filename, dots):
    """Write every dot as one line 'x,y,size,colour'. "w" replaces the old file."""
    with open(filename, "w") as file:
        for dot in dots:
            file.write(f"{dot[0]},{dot[1]},{dot[2]},{dot[3]}\n")


def draw_dots(pen, dots):
    """Jump to each dot's place and stamp a dot of its size and colour."""
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
