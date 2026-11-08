# Bug Hunt 1: Score Keeper
# This class has 3 bugs. Run it, read the red error message, and use the
# Thonny debugger (the bug button, then Step into / Step over) to find them.
# Expected output when fixed:  Comet has 10 points


class ScoreKeeper:
    """Keeps one player's score and remembers every change so it can undo."""

    def __init__(self, nickname):
        self.nickname = nickname
        self.score = 0
        self.history = []

    def add(points):
        self.score = self.score + points
        self.history.append(points)

    def undo_last(self):
        if len(self.history) > 0:
            last = self.history.pop()
            score -= last

    def report(self):
        return f"{nickname} has {self.score} points"


if __name__ == "__main__":
    keeper = ScoreKeeper("Comet")
    keeper.add(10)
    keeper.add(5)
    keeper.undo_last()
    print(keeper.report())
