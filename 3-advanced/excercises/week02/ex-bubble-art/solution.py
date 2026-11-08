# Bubble Art - reference solution
# Each Bubble object remembers its own position, size and colour.
# The draw method uses a turtle to paint the bubble on the screen.

import random
import turtle

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7"]


class Bubble:
    """Blueprint for one bubble."""

    def __init__(self, x, y, size, colour):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour

    def grow(self, amount):
        """Make the bubble bigger."""
        self.size = self.size + amount

    def move(self, dx, dy):
        """Slide the bubble by dx (right) and dy (up)."""
        self.x = self.x + dx
        self.y = self.y + dy

    def draw(self, t):
        """Paint the bubble: a big dot plus a small white shine."""
        t.penup()
        t.goto(self.x, self.y)
        t.dot(self.size, self.colour)
        t.goto(self.x - self.size / 5, self.y + self.size / 5)
        t.dot(self.size / 4, "white")


def make_bubbles(count):
    """Return a list of count Bubble objects in random places."""
    bubbles = []
    for _ in range(count):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        size = random.randint(20, 80)
        colour = random.choice(PALETTE)
        bubbles.append(Bubble(x, y, size, colour))
    return bubbles


def draw_all(bubbles, t):
    """Ask every bubble to draw itself."""
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
