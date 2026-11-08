"""Maze Muncher - the turtle VIEW (drawing, keys and the game clock).

Eat every pellet (small dots) before the ghosts catch you.
  Arrow keys or W A S D : move the muncher (P)
  Space                 : next level (after you clear one)
  R                     : play again (after you are caught or win)

Every character has a shape AND a letter, so nobody needs to tell colors
apart: P = player (circle), G = ghost (triangle), C = chaser (diamond).
All the rules live in muncher_model.py, which has its own tests.
"""

import turtle
from pathlib import Path

import muncher_model as model

HERE = Path(__file__).resolve().parent
LEVEL_FILES = [HERE / "levels" / "level1.txt", HERE / "levels" / "level2.txt"]
HIGH_SCORE_FILE = HERE / "high_scores.txt"

CELL = 32        # size of one square in pixels
TICK_MS = 400    # the ghosts move once every TICK_MS milliseconds

# Okabe-Ito color-blind-safe palette
WALL_COLOR = "#0072B2"     # blue
PLAYER_COLOR = "#E69F00"   # orange
GHOST_COLOR = "#56B4E9"    # sky blue
CHASER_COLOR = "#D55E00"   # vermillion
INK = "#000000"             # black: pellets, letters and messages
FONT = ("Arial", 14, "bold")


class MuncherApp:
    """Connects a model.Game to the screen. One app runs all the levels."""

    def __init__(self, screen, nickname="Player", level_files=None,
                 high_score_file=None):
        self.screen = screen
        self.nickname = nickname
        self.level_files = level_files or LEVEL_FILES
        self.high_score_file = high_score_file or HIGH_SCORE_FILE
        self.wall_pen = self.make_pen()    # draws the walls once per level
        self.sprite_pen = self.make_pen()  # redraws the rest every frame
        self.level_index = 0
        self.banked_score = 0  # points from levels already cleared
        self.clock_running = False
        self.message = ""
        self.start_level(0)

    def make_pen(self):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.speed(0)
        return pen

    # ---------------------------------------------------- grid -> screen
    def cell_center(self, pos):
        """Turn a (row, col) square into the (x, y) of its center on screen."""
        row, col = pos
        maze = self.game.maze
        left = -maze.width * CELL / 2
        top = maze.height * CELL / 2
        return left + col * CELL + CELL / 2, top - row * CELL - CELL / 2

    def polygon(self, pen, center, points, color):
        """Fill a shape given as (dx, dy) corners around a center point."""
        x, y = center
        pen.color(INK, color)
        pen.goto(x + points[0][0], y + points[0][1])
        pen.pendown()
        pen.begin_fill()
        for dx, dy in points[1:] + points[:1]:
            pen.goto(x + dx, y + dy)
        pen.end_fill()
        pen.penup()

    def letter(self, pen, center, text):
        x, y = center
        pen.goto(x, y - 9)
        pen.color(INK)
        pen.write(text, align="center", font=FONT)

    # ---------------------------------------------------- drawing
    def draw_walls(self):
        self.wall_pen.clear()
        h = CELL / 2
        square = [(-h, -h), (h, -h), (h, h), (-h, h)]
        maze = self.game.maze
        for row in range(maze.height):
            for col in range(maze.width):
                if maze.is_wall((row, col)):
                    center = self.cell_center((row, col))
                    self.polygon(self.wall_pen, center, square, WALL_COLOR)

    def draw_character(self, character):
        r = CELL * 0.42
        # Check Chaser first: a Chaser is also a Ghost.
        if isinstance(character, model.Chaser):
            shape, color = [(0, r), (r, 0), (0, -r), (-r, 0)], CHASER_COLOR
        elif isinstance(character, model.Ghost):
            shape, color = [(-r, -r), (r, -r), (0, r)], GHOST_COLOR
        else:
            shape, color = None, PLAYER_COLOR
        center = self.cell_center(character.pos)
        if shape is None:  # the player is a round muncher
            self.sprite_pen.goto(center)
            self.sprite_pen.dot(CELL * 0.85, color)
        else:
            self.polygon(self.sprite_pen, center, shape, color)
        self.letter(self.sprite_pen, center, character.symbol)

    def redraw(self):
        pen = self.sprite_pen
        pen.clear()
        maze = self.game.maze
        for row in range(maze.height):
            for col in range(maze.width):
                if maze.has_pellet((row, col)):
                    pen.goto(self.cell_center((row, col)))
                    pen.dot(7, INK)
        for character in [self.game.player] + self.game.ghosts:
            self.draw_character(character)
        # Score line above the maze, message line below it.
        top = maze.height * CELL / 2
        pen.goto(0, top + 10)
        pen.color(INK)
        score = self.banked_score + self.game.score
        text = f"Level {self.level_index + 1}   Score {score}"
        pen.write(text, align="center", font=FONT)
        pen.goto(0, -top - 34)
        pen.write(self.message, align="center", font=FONT)
        self.screen.update()

    # ---------------------------------------------------- game flow
    def start_level(self, index):
        self.level_index = index
        self.game = model.Game(model.load_maze(self.level_files[index]))
        self.message = "Arrow keys to move. Eat every dot!"
        self.score_saved = False
        self.draw_walls()
        self.redraw()
        if not self.clock_running:  # never start two clocks at once
            self.clock_running = True
            self.screen.ontimer(self.tick, TICK_MS)

    def tick(self):
        self.game.tick()
        self.after_change()
        if self.game.state == "playing":
            self.screen.ontimer(self.tick, TICK_MS)
        else:
            self.clock_running = False

    def on_key(self, direction):
        self.game.move_player(direction)
        self.after_change()

    def after_change(self):
        """Check for the end of a level, then redraw."""
        state = self.game.state
        last_level = self.level_index + 1 == len(self.level_files)
        if state == "won" and not last_level:
            self.message = "Level cleared! Press SPACE for the next level."
        elif state in ("won", "lost") and not self.score_saved:
            self.score_saved = True  # save once, not on every key press
            final = self.banked_score + self.game.score
            best = model.add_high_score(self.high_score_file,
                                        self.nickname, final)
            words = "You cleared every level!" if state == "won" else "Caught!"
            self.message = (f"{words} Best score: {best[0][1]}."
                            " Press R to play again.")
        self.redraw()

    def next_level(self):
        more_levels = self.level_index + 1 < len(self.level_files)
        if self.game.state == "won" and more_levels:
            self.banked_score += self.game.score
            self.start_level(self.level_index + 1)

    def restart(self):
        if self.game.state in ("won", "lost"):
            self.banked_score = 0
            self.start_level(0)

    # One small method per direction, so each key has a handler to call.
    def go_up(self):
        self.on_key("up")

    def go_down(self):
        self.on_key("down")

    def go_left(self):
        self.on_key("left")

    def go_right(self):
        self.on_key("right")

    def bind_keys(self):
        keys = [("Up", self.go_up), ("Down", self.go_down),
                ("Left", self.go_left), ("Right", self.go_right),
                ("w", self.go_up), ("s", self.go_down),
                ("a", self.go_left), ("d", self.go_right),
                ("space", self.next_level), ("r", self.restart)]
        for key, handler in keys:
            self.screen.onkey(handler, key)
        self.screen.listen()


def start(nickname="Player", level_files=None, high_score_file=None):
    """Set up the window and start the game. Returns the app (for tests)."""
    screen = turtle.Screen()
    screen.title("Maze Muncher")
    screen.setup(640, 480)
    screen.bgcolor("white")
    screen.tracer(0)  # draw whole frames at once (no flicker)
    app = MuncherApp(screen, nickname, level_files, high_score_file)
    app.bind_keys()
    return app


if __name__ == "__main__":
    name = turtle.textinput("Maze Muncher",
                            "Your nickname (not your real name):")
    start(name or "Player")
    turtle.done()
