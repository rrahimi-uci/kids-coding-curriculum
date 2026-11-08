# TEACHER REFERENCE SOLUTION: Bug Hunt 1 - Score Keeper (forgot self)
#
# What the program does: a ScoreKeeper object remembers one player's name,
# their score, and every change, so the last change can be undone. Run
# prints "Comet has 10 points" (10 + 5, then undo the 5).
# Key idea: inside a class, an object reaches its OWN data through "self".
# Approach: all three bugs are the same mistake, a missing "self". Each fix
# below adds it back, so the method talks about this particular object.
#
# The three bugs (marked FIX below):
#   FIX 1: def add(points)       -> def add(self, points)
#   FIX 2: score -= last         -> self.score -= last
#   FIX 3: {nickname} in report  -> {self.nickname}


class ScoreKeeper:
    """Keeps one player's score and remembers every change so it can undo."""

    def __init__(self, nickname):
        self.nickname = nickname
        self.score = 0
        self.history = []

    # FIX 1: Python hands the object to every method as the first
    # parameter. Without "self" here, keeper.add(10) sent the object in as
    # "points" and then complained about the extra 10.
    def add(self, points):
        self.score = self.score + points
        self.history.append(points)  # remember the change so undo can find it

    def undo_last(self):
        # Only undo if there is something to undo; pop() on an empty list
        # would crash.
        if len(self.history) > 0:
            last = self.history.pop()
            # FIX 2: plain "score" is a brand-new variable that does not
            # exist yet. The object's score is "self.score".
            self.score -= last

    def report(self):
        # FIX 3: "nickname" alone is not defined here; it is stored in self.
        return f"{self.nickname} has {self.score} points"


if __name__ == "__main__":
    keeper = ScoreKeeper("Comet")
    keeper.add(10)
    keeper.add(5)
    keeper.undo_last()
    print(keeper.report())


# Common mistakes children make here:
#   - Fixing only the first error Python shows: each run reveals the next
#     missing "self", so it takes three rounds.
#   - Writing "self.add(self, points)" or "def add(self.points)" while
#     trying to add self.
#   - Using "self" when calling the method but not when defining it, or
#     the other way round.
#
# Another correct way: undo with a one-line subtraction of the popped value.
#   self.score -= self.history.pop()
