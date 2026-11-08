"""Checks for Homework 7 - Game Idea Notebook (uses empty test folders)."""


def test_ideas_are_saved_and_loaded_in_order(load_target, tmp_path):
    notebook = load_target()
    filename = str(tmp_path / "ideas.txt")
    notebook.add_idea(filename, "A dragon racing game")
    notebook.add_idea(filename, "Rainbow spiral art")
    ideas = notebook.load_ideas(filename)
    assert ideas == ["A dragon racing game", "Rainbow spiral art"], (
        f"I added two ideas and loaded {ideas}. Use \"a\" to add and strip() when you read."
    )


def test_missing_file_gives_an_empty_list(load_target, tmp_path):
    notebook = load_target()
    missing = tmp_path / "nothing_here.txt"
    ideas = notebook.load_ideas(str(missing))
    assert ideas == [], f"A missing file should give [], not {ideas}. Did you catch FileNotFoundError?"
    assert missing.exists(), "load_ideas() should make an empty file when it is missing."


def test_the_menu_saves_and_lists_an_idea(run_target, tmp_path):
    answers = ["a", "Robot pet that tells jokes", "l", "q"]
    result = run_target(inputs=answers, cwd=tmp_path)
    saved = tmp_path / "game_ideas.txt"
    assert saved.exists() and "Robot pet that tells jokes" in saved.read_text(), (
        "After typing a and an idea, it should be saved in game_ideas.txt."
    )
    assert "1. Robot pet that tells jokes" in result.stdout, "Typing l should list the ideas with numbers."
