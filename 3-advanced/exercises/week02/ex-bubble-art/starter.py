# Bubble Art - YOUR version
# Each Bubble object remembers its own position, size and color.
# The draw method uses a turtle to paint the bubble on the screen.
# Finish the TODOs, then open check_my_work.py and press Run.

import random
import turtle

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7"]


class Bubble:
    """Blueprint for one bubble."""

    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        # TODO 1: remember size and color too (self.size = ..., self.color = ...)

    def grow(self, amount):
        """Make the bubble bigger."""
        # TODO 2: add amount to self.size
        pass

    def move(self, dx, dy):
        """Slide the bubble by dx (right) and dy (up)."""
        # TODO 3: add dx to self.x and dy to self.y
        pass

    def draw(self, t):
        """Paint the bubble: a big dot plus a small white shine."""
        t.penup()
        t.goto(self.x, self.y)
        # TODO 4: draw a dot of size self.size in self.color
        #         hint: t.dot(size, color)
        t.goto(self.x - 10, self.y + 10)
        t.dot(10, "white")


def make_bubbles(count):
    """Return a list of count Bubble objects in random places."""
    bubbles = []
    # TODO 5: repeat count times: pick a random x (-300 to 300), y (-200 to 200),
    #         size (20 to 80) and color (random.choice(PALETTE)),
    #         then append Bubble(x, y, size, color) to bubbles.
    #         (0, 0) is the middle of the window. A minus sign means "left of
    #         the middle" for x and "below the middle" for y, so x = -300 is
    #         300 steps to the left. random.randint(-300, 300) works fine.
    return bubbles


def draw_all(bubbles, t):
    """Ask every bubble to draw itself. (Already done!)"""
    for bubble in bubbles:
        bubble.draw(t)


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Bubble Art")
    screen.bgcolor("black")
    screen.tracer(0)  # draw everything at once
    pen = turtle.Turtle()
    pen.hideturtle()

    bubbles = make_bubbles(40)
    for bubble in bubbles:
        if bubble.size < 40:
            bubble.grow(10)  # small bubbles grow a little
        bubble.move(0, 30)   # every bubble floats up
    draw_all(bubbles, pen)
    screen.update()
    turtle.done()
