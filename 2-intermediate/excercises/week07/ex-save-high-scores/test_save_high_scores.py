"""Checks for Exercise 7.1 - Save High Scores.

Every check uses a brand-new empty test folder (tmp_path), so your real
high_scores.txt is never touched.
"""


def test_save_then_load_gives_the_score_back(load_target, tmp_path):
    game = load_target()
    filename = str(tmp_path / "scores.txt")
    game.save_score(filename, "Ada", 120)
    scores = game.load_scores(filename)
    assert scores == [["Ada", 120]], (
        f"I saved Ada with 120, then loaded the file and got {scores}. "
        "Expected [['Ada', 120]] (and the score must be an int: use int(parts[1]))."
    )


def test_saving_twice_keeps_both_scores(load_target, tmp_path):
    game = load_target()
    filename = str(tmp_path / "scores.txt")
    game.save_score(filename, "Kai", 95)
    game.save_score(filename, "Mei", 140)
    scores = game.load_scores(filename)
    assert scores == [["Kai", 95], ["Mei", 140]], (
        f"After saving Kai then Mei I loaded {scores}. "
        "If only Mei is left, you opened the file with \"w\" (which wipes it). Use \"a\" to add."
    )


def test_missing_file_gives_an_empty_list_and_is_created(load_target, tmp_path):
    game = load_target()
    missing = tmp_path / "no_such_file.txt"
    scores = game.load_scores(str(missing))
    assert scores == [], f"A missing file should give an empty list [], not {scores}."
    assert missing.exists(), "When the file is missing, load_scores() should make an empty one (TODO 3)."


def test_blank_lines_and_spaces_are_skipped(load_target, tmp_path):
    game = load_target()
    filename = tmp_path / "scores.txt"
    filename.write_text("Zoe,80\n\n  Omar,150  \n")
    scores = game.load_scores(str(filename))
    assert scores == [["Zoe", 80], ["Omar", 150]], (
        f"The file has an empty line and extra spaces. I expected [['Zoe', 80], ['Omar', 150]] "
        f"but got {scores}. Use line.strip() and skip lines that are empty."
    )


def test_the_game_saves_to_high_scores_txt(run_target, tmp_path):
    run_target(inputs=["Priya"], seed=7, cwd=tmp_path)
    run_target(inputs=["Leo"], seed=8, cwd=tmp_path)
    saved = tmp_path / "high_scores.txt"
    assert saved.exists(), "After a game, there should be a file called high_scores.txt."
    text = saved.read_text()
    assert "Priya," in text and "Leo," in text, (
        f"After two games, both nicknames should be in high_scores.txt. The file contains: {text!r}"
    )
