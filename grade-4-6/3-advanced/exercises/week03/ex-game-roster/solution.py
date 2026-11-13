"""TEACHER REFERENCE SOLUTION: Game Roster

What the program does: a Game keeps a roster (a list) of Player objects. It can add a
player, give points to a player by nickname, tell who is leading and list the players who
still have lives left.

Key ideas practiced: composition (a Game HAS players, unlike inheritance where something IS
a parent), a list that holds objects, searching a list, and "best so far" tracking.

Approach: Player is already finished. Game does not copy any player data; it only keeps
the Player objects and asks them to do things (add_points, is_out). give_points reuses
find, and leader keeps a "best so far" while looping.
"""


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
        # Step 1: returning the player lets the caller keep using it right away.
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
        # Step 2: find() answers None for an unknown nickname. Calling a method on None
        # would crash the program, so check first and quietly do nothing instead.
        player = self.find(nickname)
        if player is not None:
            player.add_points(points)

    def leader(self):
        """Return the Player with the highest score (None if no players)."""
        best = None
        # Step 3: keep the best player seen so far. The first player always becomes
        # "best" (nothing to beat yet); after that, only a strictly higher score wins,
        # so on a tie the player who joined first stays the leader.
        for player in self.players:
            if best is None or player.score > best.score:
                best = player
        return best

    def still_playing(self):
        """Return a list of the players who still have lives."""
        playing = []
        # Step 4: ask each Player about itself with is_out(); the Game does not need to
        # know HOW a player decides it is out.
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
    if game.find("StarFox") is not None:
        for _ in range(3):
            game.find("StarFox").lose_life()
    print(f"{game.title}: {len(game.players)} players")
    if game.leader() is not None:
        print("Leader:", game.leader().nickname)
    print("Still playing:", [p.nickname for p in game.still_playing()])


# Common mistakes children make here:
# - In add_player, creating the Player but forgetting append (the list stays empty) or
#   forgetting return player.
# - In leader, starting with best = 0 and comparing scores to it; then best is a number
#   and best.nickname crashes. best must be a Player (or None).
# - In give_points, not handling a nickname that does not exist.
# - Writing player.is_out without parentheses: a method object is always "true", so nobody
#   is ever counted as out.
#
# Another correct way for leader (built-in max picks the player with the highest score):
#     if not self.players:
#         return None
#     return max(self.players, key=lambda player: player.score)
