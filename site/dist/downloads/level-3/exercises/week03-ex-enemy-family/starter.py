# Enemy Family - YOUR version
# Inheritance: every enemy type IS AN Enemy, so it gets Enemy's code for free.
# Each child class overrides move() to move in its own way (polymorphism).
# Finish the TODOs, then press Run and see if it does what the README says.


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
    """A Guard stands still. It overrides move() but still counts its turns.
    (Already done - use it as an example!)"""

    def move(self):
        self.steps = self.steps + 1


class Zigzagger(Enemy):
    """Moves right like a normal Enemy, but also goes up, down, up, down..."""

    # TODO 1: write a move(self) method that
    #   - first calls super().move()  (x + 1 and steps + 1)
    #   - then: if self.steps is odd (self.steps % 2 == 1) add 1 to self.y,
    #           otherwise take 1 away from self.y
    pass


class Sprinter(Enemy):
    """A fast enemy. It has an extra attribute: speed."""

    def __init__(self, name, x=0, y=0, speed=3):
        # TODO 2: call super().__init__(name, x, y) so Enemy sets name, x, y, steps
        self.speed = speed

    # TODO 3: write a move(self) method that adds self.speed to self.x
    #         and adds 1 to self.steps


def move_all(enemies):
    """Move every enemy once. Each one moves in its OWN way."""
    # TODO 4: loop over enemies and call move() on each one
    pass


if __name__ == "__main__":
    enemies = [Enemy("Blob"), Guard("Rocky"), Zigzagger("Zig"), Sprinter("Zoom", speed=2)]
    for turn in range(1, 5):
        move_all(enemies)
        places = []
        for enemy in enemies:
            places.append(enemy.describe())
        print(f"Turn {turn}: " + " | ".join(places))
