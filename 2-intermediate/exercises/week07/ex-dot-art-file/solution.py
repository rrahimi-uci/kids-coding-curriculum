# TEACHER REFERENCE SOLUTION: Exercise 7.3 - Dot Art from a File
#
# What it does: draws a picture made of colored dots. The dots are NOT in
# the code: they live in the text file my_art.txt, one dot per line, written
# as   x,y,size,color   (for example   -150,-60,40,#009E73).
# Key ideas: reading and writing text files, split(","), turning text into
# numbers with int(), and keeping data (the file) apart from code.
# Approach: parse_line() turns one line of text into a dot, load_dots() does
# that for every non-empty line, and save_dots() writes dots back with "w" so
# a saved design replaces the old one. Change the file, change the picture.

import turtle

ART_FILE = "my_art.txt"


def parse_line(line):
    """Turn '-150,-60,40,#009E73' into [-150, -60, 40, '#009E73']."""
    # strip() removes the "\n" at the end; split(",") cuts the text at commas.
    parts = line.strip().split(",")
    # Everything read from a file is text. x, y and size must be numbers, or
    # the turtle cannot use them. The color stays as text on purpose.
    return [int(parts[0]), int(parts[1]), int(parts[2]), parts[3]]


def load_dots(filename):
    """Return a list of dots (one [x, y, size, color] per line). Skip empty lines."""
    dots = []
    # "with" closes the file for us when we are done, even if something fails.
    with open(filename, "r") as file:
        for line in file:
            # An empty line would crash parse_line (there is nothing to split),
            # so we skip lines with nothing but spaces.
            if line.strip() != "":
                dots.append(parse_line(line))
    return dots


def save_dots(filename, dots):
    """Write every dot as one line 'x,y,size,color'. "w" replaces the old file."""
    # "w" wipes the old file first. That is what we want: a saved design
    # replaces the old one. With "a" the dots would pile up on every save.
    with open(filename, "w") as file:
        for dot in dots:
            # "\n" ends the line, so each dot gets a line of its own.
            file.write(f"{dot[0]},{dot[1]},{dot[2]},{dot[3]}\n")


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
    pen.penup()                      # pen up, so moving between dots draws no lines

    dots = load_dots(ART_FILE)
    draw_dots(pen, dots)
    pen.goto(0, -200)
    pen.write(f"{len(dots)} dots loaded from {ART_FILE}", align="center",
              font=("Arial", 14, "normal"))
    turtle.done()


# Common mistakes children make here:
# - Forgetting int(): the dots then hold text like "-150", and pen.goto()
#   crashes or draws nothing.
# - Using "a" instead of "w" in save_dots(). Every save then adds the whole
#   picture again, so the file doubles in size each time.
# - Not skipping empty lines: a blank line at the end of my_art.txt makes
#   parse_line() fail with an IndexError.
# - Wrong index, e.g. parts[3] for the size: the order is x, y, size, color.
#
# Another correct way: unpack the pieces into named variables, which is easier to read:
#     x, y, size, color = line.strip().split(",")
#     return [int(x), int(y), int(size), color]
