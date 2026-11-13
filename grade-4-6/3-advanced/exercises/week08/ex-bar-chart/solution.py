# TEACHER REFERENCE SOLUTION: Exercise 8.3 - Bar chart
#
# What the program does: counts the survey votes for each favorite game and
# draws a bar chart with turtle: tallest bar first, the NUMBER written on
# top of each bar and the NAME written underneath.
# Key ideas: scaling a value to fit a picture, drawing from data, and
# making a chart readable without relying on color alone.
# Approach: bar_height scales each count against the biggest count, so the
# biggest bar is exactly MAX_HEIGHT tall and every other bar is in the
# right proportion. Inside the loop, write_at puts the labels in place.

import csv
import turtle

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]
FILENAME = "favorite_games.csv"

BAR_WIDTH = 80
GAP = 25
MAX_HEIGHT = 250      # the tallest bar is this many pixels high
BOTTOM = -150         # y position of the bottom of the bars


def count_games(filename):
    """Read the survey and count votes per game (the 8.1 + 8.2 work)."""
    counts = {}
    with open(filename, newline="") as f:
        for row in csv.DictReader(f):
            game = row["favorite_game"].strip().title()
            if game:
                counts[game] = counts.get(game, 0) + 1
    return counts


def bar_height(value, biggest):
    """Scale a value so the biggest value gets MAX_HEIGHT pixels."""
    # value / biggest is a share between 0 and 1 (the biggest one is 1).
    # Multiplying by MAX_HEIGHT turns that share into pixels. A value half
    # the size of the biggest therefore gets a bar half as tall.
    return value / biggest * MAX_HEIGHT


def draw_bar(t, x, height, color):
    """A filled rectangle with its bottom-left corner at (x, BOTTOM)."""
    # (Given code.) The sides go width, height, width, height, turning left
    # each time, which draws a rectangle.
    t.penup()
    t.goto(x, BOTTOM)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for side in [BAR_WIDTH, height, BAR_WIDTH, height]:
        t.forward(side)
        t.left(90)
    t.end_fill()


def write_at(t, x, y, text, size=12):
    # (Given code.) Move without drawing, then write the text centered on x.
    t.penup()
    t.goto(x, y)
    t.write(text, align="center", font=("Arial", size, "normal"))


def draw_bar_chart(t, counts, title):
    """Draw one labeled bar per item in the counts dictionary."""
    biggest = max(counts.values())  # the tallest bar is based on this one
    total_width = len(counts) * (BAR_WIDTH + GAP) - GAP
    x = -total_width / 2  # start left of center so the chart ends up centered
    # biggest bar first: sorted() with key= (from week 5!)
    items = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    for i, (name, value) in enumerate(items):
        height = bar_height(value, biggest)
        draw_bar(t, x, height, PALETTE[i % len(PALETTE)])
        middle = x + BAR_WIDTH / 2  # labels are centered on the bar
        # Number on top (a little above the bar, so it does not touch it).
        # str() turns the number into text, so we clearly write a label.
        write_at(t, middle, BOTTOM + height + 5, str(value))
        # Name underneath. With names AND numbers written out, nobody has to
        # tell the bar colors apart to read the chart.
        write_at(t, middle, BOTTOM - 25, name, size=11)
        x += BAR_WIDTH + GAP
    write_at(t, 0, BOTTOM + MAX_HEIGHT + 40, title, size=18)


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Data detectives: bar chart")
    screen.setup(800, 600)
    screen.tracer(0)
    pen = turtle.Turtle()
    pen.hideturtle()
    votes = count_games(FILENAME)
    draw_bar_chart(pen, votes, "Our favorite games (votes)")
    screen.update()
    turtle.done()


# Common mistakes children make here:
#   - Dividing whole numbers the wrong way round (biggest / value), which
#     makes the biggest bar the SHORTEST.
#   - Writing every label at the same x (for example 0) instead of at
#     middle, so all the names pile up on top of each other.
#   - Writing the number at y = BOTTOM instead of BOTTOM + height + 5, so
#     every number lands at the bottom of the chart, not on top of its bar.
#
# Another correct way: scale with the whole share first, in two steps.
#   share = value / biggest
#   return share * MAX_HEIGHT
