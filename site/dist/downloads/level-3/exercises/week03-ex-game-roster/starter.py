# Game Roster - YOUR version
# Composition: a Game HAS A list of Player objects.
# (Inheritance is "IS A"; composition is "HAS A".)
# Finish the TODOs, then press Run and see if it does what the README says.


class Player:
    """One player in the game, known by a nickname. (Already done!)"""

    def __init__(self, nickname):
        self.nickname = nickname
        self.score = 0
        self.lives = 3

    def add_points(self, points):
        self.score = self.score + points

    def lose_life(self):
        if self.lives > 0:
            self.lives = self.lives - 1

    def is_out(self):
        return self.lives == 0


class Game:
    """A game that keeps a list of Player objects."""

    def __init__(self, title):
        self.title = title
        self.players = []  # the Game HAS players

    def add_player(self, nickname):
        """Make a new Player, keep it in the list, and return it."""
        # TODO 1: make Player(nickname), append it to self.players, return it
        return None

    def find(self, nickname):
        """Return the Player with this nickname, or None. (Already done!)"""
        for player in self.players:
            if player.nickname == nickname:
                return player
        return None

    def give_points(self, nickname, points):
        # TODO 2: find the player; if it is not None, call its add_points
        pass

    def leader(self):
        """Return the Player with the highest score (None if no players)."""
        best = None
        # TODO 3: loop over self.players; keep the one with the biggest score
        return best

    def still_playing(self):
        """Return a list of the players who still have lives."""
        playing = []
        # TODO 4: append every player whose is_out() is False
        return playing


if __name__ == "__main__":
    game = Game("Space Race")
    for nickname in ["StarFox", "Comet", "Nova"]:
        game.add_player(nickname)
    game.give_points("Comet", 50)
    game.give_points("Nova", 30)
    if game.find("StarFox") is not None:
        for _ in range(3):
            game.find("StarFox").lose_life()
    print(f"{game.title}: {len(game.players)} players")
    if game.leader() is not None:
        print("Leader:", game.leader().nickname)
    print("Still playing:", [p.nickname for p in game.still_playing()])
