"""Checks for Bug Hunt 3 - Word Finder."""

WORDS = ["apple", "banana", "cherry", "dragon", "eagle", "falcon",
         "guitar", "harbor", "island", "jungle", "koala", "lemon"]


def test_finds_every_word(load_target):
    finder = load_target()
    for index, word in enumerate(WORDS):
        found = finder.find_word(WORDS, word)
        assert found == index, f"{word!r} is at index {index}, but find_word returned {found}."


def test_missing_words_give_minus_one(load_target):
    finder = load_target()
    for word in ["aardvark", "cat", "zebra"]:
        found = finder.find_word(WORDS, word)
        assert found == -1, f"{word!r} is not in the list, so the answer should be -1, not {found}."


def test_tiny_lists(load_target):
    finder = load_target()
    assert finder.find_word(["solo"], "solo") == 0, "A list with one word should still find it (index 0)."
    assert finder.find_word([], "solo") == -1, "An empty list finds nothing: -1."
