# Bar chart
# Turn the survey counts into a picture. Every bar gets:
#   - a height that matches its number (bigger number = taller bar)
#   - the NAME written under it and the NUMBER written on top,
# so nobody has to tell colours apart to read the chart.

import csv
import turtle

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]
FILENAME = "favourite_games.csv"

BAR_WIDTH = 80
GAP = 25
MAX_HEIGHT = 250      # the tallest bar is this many pixels high
BOTTOM = -150         # y position of the bottom of the bars


def count_games(filename):
    """Read the survey and count votes per game (the 8.1 + 8.2 work)."""
    counts = {}
    with open(filename, newline="") as f:
        for row in csv.DictReader(f):
            game = row["favourite_game"].strip().title()
            if game:
                counts[game] = counts.get(game, 0) + 1
    return counts


def bar_height(value, biggest):
    """Scale a value so the biggest value gets MAX_HEIGHT pixels."""
    # TODO 1: every bar is the same height! Return
    #         value / biggest * MAX_HEIGHT  so the biggest bar is MAX_HEIGHT tall.
    return MAX_HEIGHT


def draw_bar(t, x, height, colour):
    """A filled rectangle with its bottom-left corner at (x, BOTTOM)."""
    t.penup()
    t.goto(x, BOTTOM)
    t.setheading(0)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    for side in [BAR_WIDTH, height, BAR_WIDTH, height]:
        t.forward(side)
        t.left(90)
    t.end_fill()


def write_at(t, x, y, text, size=12):
    t.penup()
    t.goto(x, y)
    t.write(text, align="center", font=("Arial", size, "normal"))


def draw_bar_chart(t, counts, title):
    """Draw one labelled bar per item in the counts dictionary."""
    biggest = max(counts.values())
    total_width = len(counts) * (BAR_WIDTH + GAP) - GAP
    x = -total_width / 2
    # biggest bar first: sorted() with key= (from week 5!)
    items = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    for i, (name, value) in enumerate(items):
        height = bar_height(value, biggest)
        draw_bar(t, x, height, PALETTE[i % len(PALETTE)])
        middle = x + BAR_WIDTH / 2
        # TODO 2: use write_at() to write str(value) just above the bar
        #         (y = BOTTOM + height + 5)
        # TODO 3: use write_at() to write the name under the bar
        #         (y = BOTTOM - 25)
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
    draw_bar_chart(pen, votes, "Our favourite games (votes)")
    screen.update()
    turtle.done()
