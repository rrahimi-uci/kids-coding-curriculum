"""Maze Muncher - the game LOGIC (no turtle in this file).

Everything here is plain Python, so pytest can check every rule without
opening a window. The drawing lives in maze_muncher.py.

Positions are (row, col) pairs, just like grid[row][col]:
row 0 is the top line of the level file, col 0 is the left edge.
"""

import random
from collections import deque
from pathlib import Path

WALL = "#"
PELLET = "."
EMPTY = " "
PELLET_POINTS = 10

# How each direction changes (row, col). Up means "one row higher on screen".
DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


# ---------------------------------------------------------------- the maze
class Maze:
    """A grid of walls and pellets, read from the lines of a level file.

    Letters in the file mark where characters start:
    P = player, G = ghost (wanders), C = chaser (hunts you with BFS).
    Every start square also gets a pellet underneath, except the player's.
    """

    def __init__(self, lines):
        lines = [line.rstrip("\n") for line in lines if line.strip()]
        if not lines:
            raise ValueError("The level is empty.")
        self.width = max(len(line) for line in lines)
        self.height = len(lines)
        self.grid = []  # a 2D list: self.grid[row][col] is "#", "." or " "
        self.starts = {"P": [], "G": [], "C": []}
        for row, line in enumerate(lines):
            line = line.ljust(self.width, WALL)  # pad short rows with walls
            cells = []
            for col, char in enumerate(line):
                if char in self.starts:
                    self.starts[char].append((row, col))
                    char = EMPTY if char == "P" else PELLET
                elif char not in (WALL, PELLET):
                    char = EMPTY  # unknown letters become empty floor
                cells.append(char)
            self.grid.append(cells)
        if len(self.starts["P"]) != 1:
            raise ValueError("A level needs exactly one P (the player).")

    def in_bounds(self, pos):
        row, col = pos
        return 0 <= row < self.height and 0 <= col < self.width

    def is_wall(self, pos):
        """Outside the grid counts as a wall: nobody walks off the edge."""
        if not self.in_bounds(pos):
            return True
        row, col = pos
        return self.grid[row][col] == WALL

    def has_pellet(self, pos):
        row, col = pos
        return self.in_bounds(pos) and self.grid[row][col] == PELLET

    def eat_pellet(self, pos):
        """Remove the pellet at pos. Returns True if there was one to eat."""
        if self.has_pellet(pos):
            row, col = pos
            self.grid[row][col] = EMPTY
            return True
        return False

    def pellets_left(self):
        return sum(row.count(PELLET) for row in self.grid)

    def neighbours(self, pos):
        """The open squares next to pos, in the order up, down, left, right."""
        row, col = pos
        result = []
        for d_row, d_col in DIRECTIONS.values():
            nxt = (row + d_row, col + d_col)
            if not self.is_wall(nxt):
                result.append(nxt)
        return result

    def shortest_path(self, start, goal):
        """Breadth-first search (BFS).

        Explore the maze in rings: first every square 1 step away, then
        every square 2 steps away, and so on. A queue keeps the squares in
        the order we found them, so the first time we reach the goal we
        have found a shortest way there.

        Returns the path as a list of positions from start to goal
        (both included), or [] if the goal cannot be reached.
        """
        queue = deque([start])
        came_from = {start: None}  # square -> the square we reached it from
        while queue:
            current = queue.popleft()  # from the FRONT: first in, first out
            if current == goal:
                break
            for nxt in self.neighbours(current):
                if nxt not in came_from:  # never visit a square twice
                    came_from[nxt] = current
                    queue.append(nxt)
        if goal not in came_from:
            return []
        # Walk backwards from the goal to the start, then flip the list.
        path = []
        step = goal
        while step is not None:
            path.append(step)
            step = came_from[step]
        path.reverse()
        return path


def load_maze(filename):
    """Read a level file such as levels/level1.txt and build a Maze."""
    with open(filename, encoding="utf-8") as file:
        return Maze(file.readlines())


# ---------------------------------------------------------------- characters
class Entity:
    """Anything that stands on a square: the base class of every character."""

    symbol = "?"  # the letter drawn on screen (so we never rely on colour)

    def __init__(self, pos):
        self.pos = pos
        self.previous = pos  # where we were one move ago

    def try_move(self, maze, direction):
        """Step one square in a direction unless a wall is in the way."""
        d_row, d_col = DIRECTIONS[direction]
        target = (self.pos[0] + d_row, self.pos[1] + d_col)
        if maze.is_wall(target):
            return False
        self.previous, self.pos = self.pos, target
        return True


class Player(Entity):
    symbol = "P"


class Ghost(Entity):
    """Wanders at random but does not turn back unless it hits a dead end."""

    symbol = "G"

    def choose_step(self, maze, player_pos):
        options = maze.neighbours(self.pos)
        if len(options) > 1 and self.previous in options:
            options.remove(self.previous)
        if not options:
            return self.pos  # boxed in: stay put
        return random.choice(options)

    def take_turn(self, maze, player_pos):
        step = self.choose_step(maze, player_pos)
        self.previous, self.pos = self.pos, step


class Chaser(Ghost):
    """A ghost that always takes the first step of a shortest path to you.

    It inherits take_turn from Ghost and only changes HOW it chooses a step
    (that is overriding)."""

    symbol = "C"

    def choose_step(self, maze, player_pos):
        path = maze.shortest_path(self.pos, player_pos)
        if len(path) >= 2:
            return path[1]  # path[0] is where the chaser stands now
        return self.pos


# ---------------------------------------------------------------- the game
class Game:
    """One level: a maze, a player, some ghosts, a score and a state.

    state is "playing", "won" (all pellets eaten) or "lost" (caught)."""

    def __init__(self, maze):
        self.maze = maze  # composition: a Game HAS a Maze...
        self.player = Player(maze.starts["P"][0])  # ...and a Player...
        self.ghosts = [Ghost(pos) for pos in maze.starts["G"]]  # ...and ghosts
        self.ghosts += [Chaser(pos) for pos in maze.starts["C"]]
        self.score = 0
        self.state = "playing"

    def move_player(self, direction):
        if self.state != "playing":
            return
        if self.player.try_move(self.maze, direction):
            if self.maze.eat_pellet(self.player.pos):
                self.score += PELLET_POINTS
        self.check_end()

    def tick(self):
        """One beat of the game clock: every ghost takes one step."""
        if self.state != "playing":
            return
        for ghost in self.ghosts:
            # Each kind of ghost moves its own way (polymorphism).
            ghost.take_turn(self.maze, self.player.pos)
        self.check_end()

    def check_end(self):
        if any(ghost.pos == self.player.pos for ghost in self.ghosts):
            self.state = "lost"
        elif self.maze.pellets_left() == 0:
            self.state = "won"


# ---------------------------------------------------------------- high scores
def load_high_scores(filename):
    """Read "nickname,score" lines. Creates an empty file if it is missing.

    Returns a list of (nickname, score) pairs, best score first."""
    path = Path(filename)
    if not path.exists():
        path.write_text("", encoding="utf-8")
        return []
    scores = []
    for line in path.read_text(encoding="utf-8").splitlines():
        name, _, points = line.rpartition(",")
        if name and points.strip().isdigit():  # skip blank or broken lines
            scores.append((name.strip(), int(points)))
    return sorted(scores, key=lambda pair: pair[1], reverse=True)


def add_high_score(filename, nickname, score, keep=5):
    """Add a score, keep only the best "keep" scores, save, and return them."""
    nickname = nickname.replace(",", " ").strip() or "Player"
    scores = load_high_scores(filename)
    scores.append((nickname, score))
    scores = sorted(scores, key=lambda pair: pair[1], reverse=True)[:keep]
    lines = [f"{name},{points}\n" for name, points in scores]
    Path(filename).write_text("".join(lines), encoding="utf-8")
    return scores
