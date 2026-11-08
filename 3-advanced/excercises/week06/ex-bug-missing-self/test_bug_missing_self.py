"""Checks for Bug Hunt 1 - Score Keeper."""


def test_add_points(load_target):
    game = load_target()
    keeper = game.ScoreKeeper("Comet")
    keeper.add(10)
    keeper.add(5)
    assert keeper.score == 15, "add(10) then add(5) should give 15. Hint: a method's first parameter is always self."


def test_undo_last(load_target):
    game = load_target()
    keeper = game.ScoreKeeper("Comet")
    keeper.score, keeper.history = 15, [10, 5]
    keeper.undo_last()
    assert keeper.score == 10, "undo_last should take the last 5 points away. Hint: which score? self.score!"


def test_report(load_target):
    game = load_target()
    keeper = game.ScoreKeeper("Comet")
    keeper.score = 7
    assert keeper.report() == "Comet has 7 points", "report() should say 'Comet has 7 points'. Hint: the nickname lives in self."


def test_program_output(run_target):
    out = run_target().stdout
    assert "Comet has 10 points" in out, f"When you press Run it should print 'Comet has 10 points'. It printed: {out!r}"
