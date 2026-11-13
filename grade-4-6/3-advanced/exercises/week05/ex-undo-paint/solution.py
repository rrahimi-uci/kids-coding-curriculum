"""TEACHER REFERENCE SOLUTION: Undo Paint

What the program does: a tiny drawing program. The arrow keys draw a short line (a "stroke"),
c changes the color and u undoes the last stroke, as many times as you like.

Key ideas practiced: a stack (last in, first out, like a pile of plates), the four stack
actions push, pop, peek and size, and why a stack is the natural tool for "undo": the most
recent thing is always the first to be taken back.

Approach: the Stack class wraps a Python list and uses the END of the list as the top. The
Painter (already written) pushes every stroke when it draws. To undo, it pops the last
stroke, clears the screen and redraws all strokes that are still on the stack.
"""

import turtle

PALETTE = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#000000"]
COLOR_NAMES = ["blue", "vermillion", "green", "purple", "orange", "black"]
STEP = 30


class Stack:
    """Last in, first out - like a stack of plates."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Put an item on top."""
        # Step 1: the END of the list is the top of the stack, and append adds at the end.
        self.items.append(item)

    def pop(self):
        """Take the top item off and return it (None if the stack is empty)."""
        # Step 2: list.pop() on an empty list would crash, so check first.
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Look at the top item without taking it off (None if empty)."""
        # Step 3: items[-1] means "the last item". Unlike pop, it leaves the item there.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        # Step 4: how many items are on the stack.
        return len(self.items)


class Painter:
    """Draws strokes with a turtle and remembers them on a Stack."""

    def __init__(self, pen):
        self.pen = pen
        self.history = Stack()
        self.color_index = 0
        self.x = 0
        self.y = 0

    def color(self):
        return PALETTE[self.color_index]

    def next_color(self):
        self.color_index = (self.color_index + 1) % len(PALETTE)

    def draw_stroke(self, stroke):
        # A stroke is a tuple: (where it starts, where it ends, its color).
        start, end, color = stroke
        self.pen.penup()  # lift the pen to travel to the start without drawing
        self.pen.goto(start)
        self.pen.pendown()
        self.pen.color(color)
        self.pen.goto(end)

    def move(self, dx, dy):
        """Draw one stroke and push it onto the history stack."""
        start = (self.x, self.y)
        end = (self.x + dx, self.y + dy)
        stroke = (start, end, self.color())
        self.history.push(stroke)  # remember it, so undo can take it back later
        self.x, self.y = end
        self.draw_stroke(stroke)

    def undo(self):
        """Pop the last stroke and redraw everything that is left."""
        stroke = self.history.pop()  # the newest stroke is on top, so it comes off first
        if stroke is None:
            return  # nothing to undo
        self.x, self.y = stroke[0]  # go back to where that stroke started
        # The turtle cannot erase one line, so we wipe the picture and redraw the
        # strokes that are left, oldest first (the order they sit in the list).
        self.pen.clear()
        for old_stroke in self.history.items:
            self.draw_stroke(old_stroke)
        self.pen.penup()
        self.pen.goto(self.x, self.y)

    # Small methods with no inputs, so we can give them to screen.onkey
    def up(self):
        self.move(0, STEP)

    def down(self):
        self.move(0, -STEP)

    def left(self):
        self.move(-STEP, 0)

    def right(self):
        self.move(STEP, 0)


def show_help(writer, painter):
    """Write the keys and the color NAME (so color is never the only clue)."""
    writer.clear()
    writer.penup()
    writer.goto(-380, 260)
    name = COLOR_NAMES[painter.color_index]
    strokes = painter.history.size()
    writer.write(f"Arrows: draw   c: color ({name})   u: undo   strokes: {strokes}",
                 font=("Arial", 14, "normal"))


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Undo Paint")
    pen = turtle.Turtle()
    pen.shape("circle")
    pen.shapesize(0.5)
    pen.pensize(5)
    pen.speed(0)
    writer = turtle.Turtle()
    writer.hideturtle()
    painter = Painter(pen)

    def key(action):
        """Wrap an action so the help line updates after every key."""
        # screen.onkey needs a function with no inputs, so we build one for each key.
        def handler():
            action()
            show_help(writer, painter)
        return handler

    screen.onkey(key(painter.up), "Up")
    screen.onkey(key(painter.down), "Down")
    screen.onkey(key(painter.left), "Left")
    screen.onkey(key(painter.right), "Right")
    screen.onkey(key(painter.next_color), "c")
    screen.onkey(key(painter.undo), "u")
    screen.listen()
    show_help(writer, painter)
    turtle.done()


# Common mistakes children make here:
# - Using self.items.insert(0, item) or self.items[0]: that treats the FRONT of the list as
#   the top, so the oldest stroke is undone first (that is a queue, not a stack).
# - Forgetting the empty check, so pressing u too often crashes with "pop from empty list".
# - In peek, using self.items.pop(), which removes the item instead of just looking.
# - Forgetting return in pop, peek or size, so they give back None.
#
# Another correct way for pop and peek (a try/except instead of the empty check):
#     try:
#         return self.items.pop()
#     except IndexError:
#         return None
