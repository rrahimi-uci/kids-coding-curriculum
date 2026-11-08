# Hero Badge - the file you track with git in the Git Quest.
# Change the settings below, then use "git diff" to see what changed.

import turtle

BADGE_COLOUR = "#0072B2"   # blue (Okabe-Ito palette)
STAR_COLOUR = "#F0E442"    # yellow
HERO_NAME = "Captain Nova"  # a made-up hero name - never your real name
SIZE = 120


def draw_badge(t, size, colour):
    """Draw a filled circle (the badge) centred on (0, 0)."""
    t.penup()
    t.goto(0, -size)
    t.pendown()
    t.color("black", colour)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


def draw_star(t, size, colour):
    """Draw a filled five-pointed star in the middle of the badge."""
    t.penup()
    t.goto(-size / 2, size / 6)
    t.setheading(0)
    t.pendown()
    t.color("black", colour)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


def write_name(t, name, size):
    """Write the hero name under the badge."""
    t.penup()
    t.goto(0, -size - 40)
    t.color("black")
    t.write(name, align="center", font=("Arial", 20, "bold"))


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Hero Badge")
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)
    draw_badge(pen, SIZE, BADGE_COLOUR)
    draw_star(pen, SIZE, STAR_COLOUR)
    write_name(pen, HERO_NAME, SIZE)
    turtle.done()
