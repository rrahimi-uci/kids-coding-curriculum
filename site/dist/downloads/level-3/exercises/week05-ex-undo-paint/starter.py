# Undo Paint - YOUR version
# A drawing program where every stroke is pushed onto a STACK.
# Press u to undo: pop the last stroke off the stack and redraw the rest.
# Keys: arrows draw, c changes color, u undoes.
# Finish the Stack TODOs, then press Run and see if it does what the README says.

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
        # TODO 1: add item to the END of self.items (the end is the top)
        pass

    def pop(self):
        """Take the top item off and return it (None if the stack is empty)."""
        # TODO 2: if the stack is empty return None,
        #         otherwise return self.items.pop()
        return None

    def peek(self):
        """Look at the top item without taking it off (None if empty)."""
        # TODO 3: if empty return None, otherwise return the LAST item, self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        # TODO 4: return how many items are on the stack
        return 0


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
        start, end, color = stroke
        self.pen.penup()
        self.pen.goto(start)
        self.pen.pendown()
        self.pen.color(color)
        self.pen.goto(end)

    def move(self, dx, dy):
        """Draw one stroke and push it onto the history stack."""
        start = (self.x, self.y)
        end = (self.x + dx, self.y + dy)
        stroke = (start, end, self.color())
        self.history.push(stroke)
        self.x, self.y = end
        self.draw_stroke(stroke)

    def undo(self):
        """Pop the last stroke and redraw everything that is left."""
        stroke = self.history.pop()
        if stroke is None:
            return  # nothing to undo
        self.x, self.y = stroke[0]  # go back to where that stroke started
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
    writer.write(f"Arrows: draw   c: color ({name})   u: undo   strokes: {painter.history.size()}",
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
