# Enemy Family - reference solution
# Inheritance: every enemy type IS AN Enemy, so it gets Enemy's code for free.
# Each child class overrides move() to move in its own way (polymorphism).


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
        super().move()  # do the normal Enemy move first (x + 1, steps + 1)
        if self.steps % 2 == 1:
            self.y = self.y + 1
        else:
            self.y = self.y - 1


class Sprinter(Enemy):
    """A fast enemy. It has an extra attribute: speed."""

    def __init__(self, name, x=0, y=0, speed=3):
        super().__init__(name, x, y)  # let Enemy set name, x, y and steps
        self.speed = speed

    def move(self):
        self.x = self.x + self.speed
        self.steps = self.steps + 1


def move_all(enemies):
    """Move every enemy once. Each one moves in its OWN way."""
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
