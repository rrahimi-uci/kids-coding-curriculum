# Bug Hunt 1: Score Keeper - FIXED version (teacher)
# The three bugs were all "forgot self":
#   1. def add(points)        -> def add(self, points)
#   2. score -= last          -> self.score -= last
#   3. {nickname} in report   -> {self.nickname}


class ScoreKeeper:
    """Keeps one player's score and remembers every change so it can undo."""

    def __init__(self, nickname):
        self.nickname = nickname
        self.score = 0
        self.history = []

    def add(self, points):
        self.score = self.score + points
        self.history.append(points)

    def undo_last(self):
        if len(self.history) > 0:
            last = self.history.pop()
            self.score -= last

    def report(self):
        return f"{self.nickname} has {self.score} points"


if __name__ == "__main__":
    keeper = ScoreKeeper("Comet")
    keeper.add(10)
    keeper.add(5)
    keeper.undo_last()
    print(keeper.report())
