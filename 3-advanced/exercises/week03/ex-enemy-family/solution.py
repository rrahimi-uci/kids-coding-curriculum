"""TEACHER REFERENCE SOLUTION: Enemy Family

What the program does: it makes four kinds of enemy that all move differently each turn. A
plain Enemy steps right, a Guard stands still, a Zigzagger steps right and bobs up and down,
and a Sprinter takes bigger steps. `move_all` moves every enemy and each one does it its own
way.

Key ideas practiced: inheritance (a child class "is a" parent class), overriding a method,
`super()` to reuse the parent's code, and polymorphism (one call, `enemy.move()`, many
behaviors).

Approach: the parent `Enemy` holds what all enemies share. Each child changes only what is
different. Zigzagger calls `super().move()` and adds the up/down bob; Sprinter calls
`super().__init__` so the parent still sets up name, x, y and steps.
"""


class Enemy:
    """Parent class: a plain enemy walks one step to the right each turn."""

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.steps = 0

    def move(self):
        self.x = self.x + 1
        self.steps = self.steps + 1

    def describe(self):
        return f"{self.name} at ({self.x}, {self.y})"


class Guard(Enemy):
    """A Guard stands still. It overrides move() but still counts its turns."""

    def move(self):
        self.steps = self.steps + 1


class Zigzagger(Enemy):
    """Moves right like a normal Enemy, but also goes up, down, up, down..."""

    def move(self):
        # Step 1: super() means "the parent class". This reuses Enemy's move (x + 1 and
        # steps + 1), so we do not copy that code here.
        super().move()
        # steps is already counted, so turn 1 is odd (go up), turn 2 is even (go down)...
        # "% 2" gives the remainder after dividing by 2: 1 for odd numbers, 0 for even.
        if self.steps % 2 == 1:
            self.y = self.y + 1
        else:
            self.y = self.y - 1


class Sprinter(Enemy):
    """A fast enemy. It has an extra attribute: speed."""

    def __init__(self, name, x=0, y=0, speed=3):
        # Step 2: let the parent set name, x, y and steps. Without this line the Sprinter
        # would have no name (the AttributeError the README warns about).
        super().__init__(name, x, y)
        self.speed = speed  # the only thing that is new in a Sprinter

    def move(self):
        # Step 3: the same as Enemy.move, but "speed" steps instead of 1. We cannot call
        # super().move() here because that would always add exactly 1.
        self.x = self.x + self.speed
        self.steps = self.steps + 1


def move_all(enemies):
    """Move every enemy once. Each one moves in its OWN way."""
    # Step 4: we do not check which kind of enemy it is. Python picks the right move()
    # for each object. That is polymorphism.
    for enemy in enemies:
        enemy.move()


if __name__ == "__main__":
    enemies = [Enemy("Blob"), Guard("Rocky"), Zigzagger("Zig"), Sprinter("Zoom", speed=2)]
    for turn in range(1, 5):
        move_all(enemies)
        places = []
        for enemy in enemies:
            places.append(enemy.describe())
        print(f"Turn {turn}: " + " | ".join(places))


# Common mistakes children make here:
# - Forgetting `super().__init__(name, x, y)` in Sprinter, so `name` is missing.
# - In Zigzagger, forgetting `super().move()`, so it bobs up and down but never goes right.
# - Writing `move_all` with `enemy.move` (no brackets) so nothing actually moves.
# - Writing `if type(enemy) == Guard: ...` inside move_all instead of trusting move().
#
# Another correct way for the bob in Zigzagger.move (one line instead of if/else):
#     self.y = self.y + (1 if self.steps % 2 == 1 else -1)
