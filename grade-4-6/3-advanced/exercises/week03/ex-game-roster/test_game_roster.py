"""Checks for Exercise 3.3 - Game Roster."""


def make_game(roster):
    game = roster.Game("Test Cup")
    for nickname in ["Ada", "Kai", "Mei"]:
        game.add_player(nickname)
    return game


def test_add_player_keeps_player_objects(load_target):
    roster = load_target()
    game = make_game(roster)
    assert len(game.players) == 3, f"After adding 3 players the list should hold 3, not {len(game.players)}."
    assert all(isinstance(p, roster.Player) for p in game.players), "game.players should hold Player objects."
    assert isinstance(game.add_player("Zoe"), roster.Player), "add_player should return the new Player."


def test_give_points(load_target):
    roster = load_target()
    game = make_game(roster)
    game.give_points("Kai", 40)
    game.give_points("Kai", 2)
    game.give_points("Nobody", 99)  # unknown nickname: nothing happens
    assert game.find("Kai").score == 42, "Kai got 40 + 2 points, so the score should be 42."


def test_leader(load_target):
    roster = load_target()
    assert roster.Game("Empty").leader() is None, "A game with no players has no leader: return None."
    game = make_game(roster)
    game.give_points("Mei", 10)
    game.give_points("Ada", 25)
    leader = game.leader()
    assert leader is not None and leader.nickname == "Ada", "Ada has the most points, so Ada is the leader."


def test_still_playing(load_target):
    roster = load_target()
    game = make_game(roster)
    for _ in range(3):
        game.find("Ada").lose_life()
    names = [p.nickname for p in game.still_playing()]
    assert names == ["Kai", "Mei"], f"Ada has no lives left, so only Kai and Mei are still playing. Got {names}."
