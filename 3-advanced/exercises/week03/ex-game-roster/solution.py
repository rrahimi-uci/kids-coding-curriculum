# Game Roster - reference solution
# Composition: a Game HAS A list of Player objects.
# (Inheritance is "IS A"; composition is "HAS A".)


class Player:
    """One player in the game, known by a nickname."""

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
        player = Player(nickname)
        self.players.append(player)
        return player

    def find(self, nickname):
        """Return the Player with this nickname, or None."""
        for player in self.players:
            if player.nickname == nickname:
                return player
        return None

    def give_points(self, nickname, points):
        player = self.find(nickname)
        if player is not None:
            player.add_points(points)

    def leader(self):
        """Return the Player with the highest score (None if no players)."""
        best = None
        for player in self.players:
            if best is None or player.score > best.score:
                best = player
        return best

    def still_playing(self):
        """Return a list of the players who still have lives."""
        playing = []
        for player in self.players:
            if not player.is_out():
                playing.append(player)
        return playing


if __name__ == "__main__":
    game = Game("Space Race")
    for nickname in ["StarFox", "Comet", "Nova"]:
        game.add_player(nickname)
    game.give_points("Comet", 50)
    game.give_points("Nova", 30)
    for _ in range(3):
        game.find("StarFox").lose_life()
    print(f"{game.title}: {len(game.players)} players")
    print("Leader:", game.leader().nickname)
    print("Still playing:", [p.nickname for p in game.still_playing()])
