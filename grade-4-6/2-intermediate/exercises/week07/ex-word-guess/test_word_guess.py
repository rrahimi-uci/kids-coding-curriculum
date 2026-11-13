"""Checks for Exercise 7.2 - Word Guess."""

ALL_LETTERS = list("etaoinshrdlucmfwypvbgkjqxz")


def test_load_words_cleans_up_each_line(load_target, tmp_path):
    game = load_target()
    word_file = tmp_path / "test_words.txt"
    word_file.write_text("Dragon\n\n  pixel  \nROCKET\n")
    words = game.load_words(str(word_file))
    assert words == ["dragon", "pixel", "rocket"], (
        f"The file has capitals, spaces and an empty line. I expected "
        f"['dragon', 'pixel', 'rocket'] but got {words}. Use strip(), lower() and skip empty lines."
    )


def test_load_words_reads_the_real_word_file(load_target, target_path):
    game = load_target()
    words = game.load_words(str(target_path.parent / "words.txt"))
    assert len(words) >= 10, f"words.txt has at least 10 words, but load_words() found {len(words)}."
    for word in words:
        assert word.isalpha() and word == word.lower(), f"Every word should be small letters only, not {word!r}."


def test_show_progress_hides_letters_not_guessed(load_target):
    game = load_target()
    shown = game.show_progress("pixel", ["p", "e"])
    assert shown == "p _ _ e _", f'With p and e guessed, "pixel" should show "p _ _ e _", not "{shown}".'
    shown = game.show_progress("cat", [])
    assert shown == "_ _ _", f'With nothing guessed, "cat" should show "_ _ _", not "{shown}".'


def test_a_whole_game_ends_and_shows_the_word(run_target):
    result = run_target(inputs=ALL_LETTERS, seed=3)
    text = result.stdout.lower()
    assert "no words yet" not in text and "know 0 words" not in text, (
        "The game found no words. load_words() should read them from words.txt (TODO 1)."
    )
    assert "the word was" in text, "At the end of a game, tell the player what the word was."
