"""A headless stand-in for Python's ``turtle`` module.

Exercise tests swap this in for the real module so that drawing programs run
instantly, without opening a window, and so that tests can inspect what was
drawn (lines, dots, fills, text, colors, key handlers, timers...).

The geometry follows the real ``turtle`` module closely (standard mode:
heading 0 = east, ``left`` turns counter-clockwise, ``circle`` is drawn as the
same polygon the real module draws), so positions in tests match what a
student sees on screen.
"""

from __future__ import annotations

import math
import types
from dataclasses import dataclass, field

Vec = tuple  # (x, y)


class Terminator(Exception):
    """Raised by the real turtle when the window is closed. Kept for scripts
    that catch it."""


class TurtleGraphicsError(Exception):
    pass


@dataclass
class Line:
    start: Vec
    end: Vec
    color: object
    width: float

    @property
    def length(self) -> float:
        return math.dist(self.start, self.end)


@dataclass
class Dot:
    pos: Vec
    size: float
    color: object


@dataclass
class Text:
    text: str
    pos: Vec
    align: str
    font: object


@dataclass
class Fill:
    color: object
    points: list = field(default_factory=list)


def _round(v: float) -> float:
    r = round(v, 6)
    return 0.0 if r == 0 else r


class FakeScreen:
    """Records screen settings and stores event handlers so tests can fire them."""

    def __init__(self, inputs=None):
        self.bg = "white"
        self.window_title = ""
        self.size = (800, 600)
        self.tracer_n = 1
        self.update_count = 0
        self.key_handlers: dict = {}
        self.key_release_handlers: dict = {}
        self.click_handlers: list = []
        self.timers: list = []  # (due_time_ms, order, func)
        self.time_ms = 0
        self._timer_order = 0
        self.listening = False
        self.mainloop_called = False
        self.closed = False
        self.mode_value = "standard"
        self._colormode = 1.0
        self.shapes: dict = {}
        self.turtle_list: list = []
        self.inputs = list(inputs or [])
        self.prompts: list = []
        self.world = None

    # ----- appearance
    def bgcolor(self, *args):
        if not args:
            return self.bg
        self.bg = args[0] if len(args) == 1 else tuple(args)

    def bgpic(self, picname=None):
        return "nopic"

    def title(self, text):
        self.window_title = text

    def setup(self, width=800, height=600, startx=None, starty=None):
        self.size = (width, height)

    def screensize(self, canvwidth=None, canvheight=None, bg=None):
        if canvwidth is None and canvheight is None:
            return self.size
        self.size = (canvwidth or self.size[0], canvheight or self.size[1])
        if bg is not None:
            self.bg = bg

    def window_width(self):
        return self.size[0]

    def window_height(self):
        return self.size[1]

    def setworldcoordinates(self, llx, lly, urx, ury):
        self.world = (llx, lly, urx, ury)

    def colormode(self, cmode=None):
        if cmode is None:
            return self._colormode
        self._colormode = cmode

    def mode(self, mode=None):
        if mode is None:
            return self.mode_value
        self.mode_value = mode

    def register_shape(self, name, shape=None):
        self.shapes[name] = shape

    addshape = register_shape

    def getshapes(self):
        return sorted(["arrow", "turtle", "circle", "square", "triangle", "classic", *self.shapes])

    def turtles(self):
        return list(self.turtle_list)

    def delay(self, delay=None):
        return 0

    def tracer(self, n=None, delay=None):
        if n is None:
            return self.tracer_n
        self.tracer_n = n

    def update(self):
        self.update_count += 1

    def clearscreen(self):
        for t in self.turtle_list:
            t.clear()
        self.turtle_list.clear()

    clear = clearscreen

    def resetscreen(self):
        for t in self.turtle_list:
            t.reset()

    reset = resetscreen

    def getcanvas(self):
        return None

    # ----- events
    def listen(self, xdummy=None, ydummy=None):
        self.listening = True

    def onkey(self, fun, key):
        if fun is None:
            self.key_handlers.pop(key, None)
        else:
            self.key_handlers[key] = fun

    onkeyrelease = onkey

    def onkeypress(self, fun, key=None):
        if fun is None:
            self.key_handlers.pop(key, None)
        else:
            self.key_handlers[key] = fun

    def onclick(self, fun, btn=1, add=None):
        if fun is None:
            self.click_handlers.clear()
        elif add:
            self.click_handlers.append(fun)
        else:
            self.click_handlers = [fun]

    onscreenclick = onclick

    def ontimer(self, fun, t=0):
        self._timer_order += 1
        self.timers.append((self.time_ms + int(t or 0), self._timer_order, fun))

    def mainloop(self):
        self.mainloop_called = True

    done = mainloop

    def exitonclick(self):
        self.mainloop_called = True

    def bye(self):
        self.closed = True

    def textinput(self, title, prompt):
        self.prompts.append(prompt)
        if not self.inputs:
            raise AssertionError(f"The program asked for more input than the test gave it: {prompt!r}")
        return str(self.inputs.pop(0))

    def numinput(self, title, prompt, default=None, minval=None, maxval=None):
        self.prompts.append(prompt)
        if not self.inputs:
            if default is not None:
                return float(default)
            raise AssertionError(f"The program asked for more input than the test gave it: {prompt!r}")
        return float(self.inputs.pop(0))

    # ----- helpers for tests
    def press(self, key: str) -> None:
        """Simulate pressing a key (e.g. "Left", "space", "a")."""
        handler = self.key_handlers.get(key)
        if handler is None and key is not None:
            handler = self.key_handlers.get(None)
        if handler is None:
            raise AssertionError(f"Nothing happens when the {key!r} key is pressed (no onkey handler).")
        handler()

    def click(self, x: float, y: float) -> None:
        if not self.click_handlers:
            raise AssertionError("Nothing happens when the screen is clicked (no onscreenclick handler).")
        for handler in list(self.click_handlers):
            handler(x, y)

    def run_timers(self, max_steps: int = 100) -> int:
        """Run pending ontimer callbacks in time order (callbacks may schedule
        more). Returns how many callbacks ran. Stops after ``max_steps`` so
        game loops that reschedule themselves forever still finish."""
        ran = 0
        while self.timers and ran < max_steps and not self.closed:
            self.timers.sort()
            due, _order, fun = self.timers.pop(0)
            self.time_ms = max(self.time_ms, due)
            fun()
            ran += 1
        return ran

    @property
    def all_lines(self):
        return [line for t in self.turtle_list for line in t.lines]


class FakeTurtle:
    """Records everything a turtle does. Shares the API of ``turtle.Turtle``."""

    _screen: FakeScreen | None = None

    def __init__(self, shape="classic", undobuffersize=1000, visible=True, screen=None):
        self.screen = screen or FakeTurtle._screen
        self._x = 0.0
        self._y = 0.0
        self._heading = 0.0
        self._pendown = True
        self._pencolor: object = "black"
        self._fillcolor: object = "black"
        self._pensize = 1.0
        self._visible = visible
        self._speed = 3
        self._shape = shape
        self._shapesize = (1, 1, 1)
        self._filling = False
        self._current_fill: Fill | None = None
        self.lines: list[Line] = []
        self.dots: list[Dot] = []
        self.texts: list[Text] = []
        self.fills: list[Fill] = []
        self.stamps: list = []
        self.calls: list = []
        self.path: list = [(0.0, 0.0)]
        self.total_turn = 0.0  # signed degrees turned with left/right (+ = left)
        self.click_handlers: list = []
        self.drag_handlers: list = []
        if self.screen is not None:
            self.screen.turtle_list.append(self)

    # ----- internal
    def _log(self, name, *args):
        self.calls.append((name, args))

    def _move_to(self, x, y):
        start = (_round(self._x), _round(self._y))
        end = (_round(x), _round(y))
        if self._pendown and start != end:
            self.lines.append(Line(start, end, self._pencolor, self._pensize))
        if self._filling and self._current_fill is not None:
            self._current_fill.points.append(end)
        self._x, self._y = float(x), float(y)
        self.path.append(end)

    # ----- motion
    def forward(self, distance):
        self._log("forward", distance)
        rad = math.radians(self._heading)
        self._move_to(self._x + distance * math.cos(rad), self._y + distance * math.sin(rad))

    fd = forward

    def back(self, distance):
        self._log("back", distance)
        self.forward(-distance)
        self.calls.pop()

    bk = backward = back

    def left(self, angle):
        self._log("left", angle)
        self._heading = (self._heading + angle) % 360
        self.total_turn += angle

    lt = left

    def right(self, angle):
        self._log("right", angle)
        self._heading = (self._heading - angle) % 360
        self.total_turn -= angle

    rt = right

    def goto(self, x, y=None):
        if y is None:
            x, y = x
        self._log("goto", x, y)
        self._move_to(x, y)

    setpos = setposition = goto

    def teleport(self, x=None, y=None, *, fill_gap=False):
        self._log("teleport", x, y)
        self._x = float(self._x if x is None else x)
        self._y = float(self._y if y is None else y)
        self.path.append((_round(self._x), _round(self._y)))

    def setx(self, x):
        self.goto(x, self._y)

    def sety(self, y):
        self.goto(self._x, y)

    def home(self):
        self.goto(0, 0)
        self._heading = 0.0

    def setheading(self, to_angle):
        self._log("setheading", to_angle)
        self._heading = to_angle % 360

    seth = setheading

    def circle(self, radius, extent=None, steps=None):
        """Same polygon approximation as the real turtle module."""
        self._log("circle", radius, extent, steps)
        if extent is None:
            extent = 360
        if steps is None:
            frac = abs(extent) / 360
            steps = 1 + int(min(11 + abs(radius * frac) / 6.0, 59.0) * frac)
        w = 1.0 * extent / steps
        w2 = 0.5 * w
        length = 2.0 * radius * math.sin(math.radians(w2))
        if radius < 0:
            length, w, w2 = -length, -w, -w2
        turned_before = self.total_turn
        self._heading = (self._heading + w2) % 360
        for _ in range(steps):
            rad = math.radians(self._heading)
            self._move_to(self._x + length * math.cos(rad), self._y + length * math.sin(rad))
            self._heading = (self._heading + w) % 360
        self._heading = (self._heading - w2) % 360
        self.total_turn = turned_before + (extent if radius >= 0 else -extent)

    def dot(self, size=None, *color):
        if size is None:
            size = max(self._pensize + 4, 2 * self._pensize)
        col = color[0] if len(color) == 1 else (tuple(color) if color else self._pencolor)
        self._log("dot", size, col)
        self.dots.append(Dot((_round(self._x), _round(self._y)), size, col))

    def stamp(self):
        self._log("stamp")
        self.stamps.append(((_round(self._x), _round(self._y)), self._fillcolor, self._shape))
        return len(self.stamps)

    def clearstamp(self, stampid):
        pass

    def clearstamps(self, n=None):
        self.stamps.clear()

    def undo(self):
        pass

    def speed(self, speed=None):
        if speed is None:
            return self._speed
        self._speed = speed

    def degrees(self, fullcircle=360.0):
        pass

    def radians(self):
        raise TurtleGraphicsError("radians() is not supported by the test turtle")

    # ----- state
    def position(self):
        return Vec2D(_round(self._x), _round(self._y))

    pos = position

    def xcor(self):
        return _round(self._x)

    def ycor(self):
        return _round(self._y)

    def heading(self):
        return _round(self._heading)

    def towards(self, x, y=None):
        if y is None:
            x, y = x
        return math.degrees(math.atan2(y - self._y, x - self._x)) % 360

    def distance(self, x, y=None):
        if y is None:
            if isinstance(x, FakeTurtle):
                x, y = x._x, x._y
            else:
                x, y = x
        return math.dist((self._x, self._y), (x, y))

    # ----- pen
    def penup(self):
        self._log("penup")
        self._pendown = False

    pu = up = penup

    def pendown(self):
        self._log("pendown")
        self._pendown = True

    pd = down = pendown

    def isdown(self):
        return self._pendown

    def pensize(self, width=None):
        if width is None:
            return self._pensize
        self._log("pensize", width)
        self._pensize = width

    width = pensize

    def pen(self, pen=None, **pendict):
        return {"pendown": self._pendown, "pencolor": self._pencolor,
                "fillcolor": self._fillcolor, "pensize": self._pensize}

    @staticmethod
    def _norm(args):
        return args[0] if len(args) == 1 else tuple(args)

    def pencolor(self, *args):
        if not args:
            return self._pencolor
        self._log("pencolor", *args)
        self._pencolor = self._norm(args)

    def fillcolor(self, *args):
        if not args:
            return self._fillcolor
        self._log("fillcolor", *args)
        self._fillcolor = self._norm(args)

    def color(self, *args):
        if not args:
            return (self._pencolor, self._fillcolor)
        self._log("color", *args)
        if len(args) == 2:
            self._pencolor, self._fillcolor = args
        elif len(args) == 1 and isinstance(args[0], (tuple, list)) and len(args[0]) == 2 \
                and not all(isinstance(v, (int, float)) for v in args[0]):
            self._pencolor, self._fillcolor = args[0]
        else:
            self._pencolor = self._fillcolor = self._norm(args)

    def begin_fill(self):
        self._log("begin_fill")
        self._filling = True
        self._current_fill = Fill(self._fillcolor, [(_round(self._x), _round(self._y))])

    def end_fill(self):
        self._log("end_fill")
        if self._filling and self._current_fill is not None:
            self._current_fill.color = self._fillcolor
            self.fills.append(self._current_fill)
        self._filling = False
        self._current_fill = None

    def filling(self):
        return self._filling

    def write(self, arg, move=False, align="left", font=("Arial", 8, "normal")):
        self._log("write", arg)
        self.texts.append(Text(str(arg), (_round(self._x), _round(self._y)), align, font))

    def clear(self):
        self._log("clear")
        self.lines.clear()
        self.dots.clear()
        self.texts.clear()
        self.fills.clear()
        self.stamps.clear()

    def reset(self):
        self.clear()
        self._x = self._y = self._heading = 0.0
        self._pendown = True
        self.total_turn = 0.0

    # ----- appearance
    def hideturtle(self):
        self._visible = False

    ht = hideturtle

    def showturtle(self):
        self._visible = True

    st = showturtle

    def isvisible(self):
        return self._visible

    def shape(self, name=None):
        if name is None:
            return self._shape
        self._shape = name

    def shapesize(self, stretch_wid=None, stretch_len=None, outline=None):
        if stretch_wid is None and stretch_len is None and outline is None:
            return self._shapesize
        self._shapesize = (stretch_wid or 1, stretch_len or stretch_wid or 1, outline or 1)

    turtlesize = shapesize

    def tilt(self, angle):
        pass

    def settiltangle(self, angle):
        pass

    def tiltangle(self, angle=None):
        return 0.0

    # ----- events / misc
    def onclick(self, fun, btn=1, add=None):
        self.click_handlers.append(fun)

    def onrelease(self, fun, btn=1, add=None):
        pass

    def ondrag(self, fun, btn=1, add=None):
        self.drag_handlers.append(fun)

    def getscreen(self):
        return self.screen

    def clone(self):
        twin = type(self)(shape=self._shape, screen=self.screen)
        twin._x, twin._y, twin._heading = self._x, self._y, self._heading
        twin._pendown, twin._pencolor, twin._fillcolor = self._pendown, self._pencolor, self._fillcolor
        twin._pensize = self._pensize
        return twin

    def setundobuffer(self, size):
        pass

    def getpen(self):
        return self

    getturtle = getpen

    # ----- helpers for tests
    @property
    def distance_traveled(self) -> float:
        return sum(line.length for line in self.lines)

    @property
    def colors_used(self) -> set:
        cols = {line.color for line in self.lines}
        cols |= {d.color for d in self.dots}
        cols |= {f.color for f in self.fills}
        return {c if not isinstance(c, list) else tuple(c) for c in cols}

    def is_back_at_start(self, tol: float = 0.5) -> bool:
        return math.dist(self.path[0], (self._x, self._y)) <= tol

    def count(self, method: str) -> int:
        return sum(1 for name, _ in self.calls if name == method)


class Vec2D(tuple):
    """Minimal copy of turtle.Vec2D (a 2-tuple with arithmetic)."""

    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))

    def __add__(self, other):
        return Vec2D(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        return Vec2D(self[0] - other[0], self[1] - other[1])

    def __mul__(self, other):
        if isinstance(other, Vec2D):
            return self[0] * other[0] + self[1] * other[1]
        return Vec2D(self[0] * other, self[1] * other)

    __rmul__ = __mul__

    def __abs__(self):
        return math.hypot(*self)

    def __repr__(self):
        return f"({self[0]:.2f},{self[1]:.2f})"


_SCREEN_FUNCS = [
    "bgcolor", "bgpic", "title", "setup", "screensize", "window_width", "window_height",
    "setworldcoordinates", "colormode", "mode", "register_shape", "addshape", "getshapes",
    "turtles", "delay", "tracer", "update", "clearscreen", "resetscreen", "listen", "onkey",
    "onkeypress", "onkeyrelease", "onscreenclick", "ontimer", "mainloop", "done", "exitonclick",
    "bye", "textinput", "numinput", "getcanvas",
]
_TURTLE_FUNCS = [
    "forward", "fd", "back", "bk", "backward", "left", "lt", "right", "rt", "goto", "setpos",
    "setposition", "teleport", "setx", "sety", "home", "setheading", "seth", "circle", "dot",
    "stamp", "clearstamp", "clearstamps", "undo", "speed", "degrees", "position", "pos", "xcor",
    "ycor", "heading", "towards", "distance", "penup", "pu", "up", "pendown", "pd", "down",
    "isdown", "pensize", "width", "pen", "pencolor", "fillcolor", "color", "begin_fill",
    "end_fill", "filling", "write", "hideturtle", "ht", "showturtle", "st", "isvisible",
    "shape", "shapesize", "turtlesize", "tilt", "settiltangle", "tiltangle", "onclick",
    "onrelease", "ondrag", "getscreen", "clone", "setundobuffer", "getpen", "getturtle",
    "clear", "reset",
]


def make_fake_turtle_module(inputs=None) -> types.ModuleType:
    """Build a fresh fake ``turtle`` module (fresh screen, no turtles)."""
    mod = types.ModuleType("turtle")
    screen = FakeScreen(inputs=inputs)

    class Turtle(FakeTurtle):
        def __init__(self, shape="classic", undobuffersize=1000, visible=True, screen_=None):
            super().__init__(shape=shape, undobuffersize=undobuffersize, visible=visible, screen=screen)

    anon: dict = {}

    def get_anon():
        if "t" not in anon:
            anon["t"] = Turtle()
        return anon["t"]

    def Screen():  # noqa: N802 - mirrors turtle API
        return screen

    def RawTurtle(canvas=None, *args, **kwargs):  # noqa: N802
        return Turtle()

    mod.Turtle = Turtle
    mod.Pen = Turtle
    mod.RawTurtle = RawTurtle
    mod.RawPen = RawTurtle
    mod.Screen = Screen
    mod._Screen = FakeScreen
    mod.TurtleScreen = FakeScreen
    mod.Vec2D = Vec2D
    mod.Terminator = Terminator
    mod.TurtleGraphicsError = TurtleGraphicsError
    mod.FAKE = True
    mod.screen = screen
    mod.anonymous_turtle = get_anon

    for name in _SCREEN_FUNCS:
        setattr(mod, name, getattr(screen, name))
    for name in _TURTLE_FUNCS:
        def make(n):
            def func(*args, **kwargs):
                return getattr(get_anon(), n)(*args, **kwargs)
            func.__name__ = n
            return func
        if name in ("clear", "reset") and hasattr(mod, name):
            continue
        setattr(mod, name, make(name))
    mod.getturtle = mod.getpen = get_anon
    return mod
