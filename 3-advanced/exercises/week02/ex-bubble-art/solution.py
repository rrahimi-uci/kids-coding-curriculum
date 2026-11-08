"""TEACHER REFERENCE SOLUTION: Bubble Art

What the program does: it opens a black window and paints 40 colorful bubbles in random
places. Every bubble has a little white shine. Small bubbles are grown a bit, and all bubbles
float up a little before they are painted.

Key ideas practiced: a class as a blueprint, __init__ and self, methods that change an
object's own numbers, and a loop that makes many objects and keeps them in a list.

Approach: a Bubble remembers its own x, y, size and color. Its methods (grow, move,
draw) only touch self, so every bubble is independent. make_bubbles creates the objects
in a loop with random values and collects them in a list.
"""

import random
import turtle

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7"]


class Bubble:
    """Blueprint for one bubble."""

    def __init__(self, x, y, size, color):
        # Each bubble keeps its OWN copy of these four facts. "self" means "this bubble".
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def grow(self, amount):
        """Make the bubble bigger."""
        self.size = self.size + amount

    def move(self, dx, dy):
        """Slide the bubble by dx (right) and dy (up)."""
        self.x = self.x + dx
        self.y = self.y + dy

    def draw(self, t):
        """Paint the bubble: a big dot plus a small white shine."""
        # Lift the pen so moving to the bubble does not draw a line.
        t.penup()
        t.goto(self.x, self.y)
        t.dot(self.size, self.color)
        # The shine sits up and to the left of the center. Using the bubble's size (instead
        # of fixed numbers) keeps the shine in the same spot on small and big bubbles.
        t.goto(self.x - self.size / 5, self.y + self.size / 5)
        t.dot(self.size / 4, "white")


def make_bubbles(count):
    """Return a list of count Bubble objects in random places."""
    bubbles = []
    # "_" is a throw-away loop name: we only want to repeat, not use the counter.
    for _ in range(count):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        size = random.randint(20, 80)
        color = random.choice(PALETTE)
        # Every pass through the loop makes a NEW Bubble object.
        bubbles.append(Bubble(x, y, size, color))
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


# Common mistakes children make here:
# - Writing size = size or x = x in __init__ (no self.): the value is thrown away and
#   the bubble forgets it, so b.size fails.
# - Writing size + amount in grow without assigning it back to self.size.
# - Using one Bubble outside the loop and appending it 40 times: all 40 list items are the
#   same bubble. Make the Bubble INSIDE the loop.
# - Forgetting t.penup() so lines are drawn between bubbles (already done in the starter).
#
# Another correct way for make_bubbles (a list comprehension):
#     return [Bubble(random.randint(-300, 300), random.randint(-200, 200),
#                    random.randint(20, 80), random.choice(PALETTE)) for _ in range(count)]
