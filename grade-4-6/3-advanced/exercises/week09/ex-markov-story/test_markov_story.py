"""Checks for Exercise 9.3 - Markov story machine."""

import random


def test_chain_remembers_what_comes_next(load_target):
    program = load_target()
    got = program.build_chain(["a", "b", "a", "c"])
    assert got == {"a": ["b", "c"], "b": ["a"]}, \
        f"For the words a b a c the chain should be {{'a': ['b', 'c'], 'b': ['a']}}, not {got}."


def test_chain_keeps_repeats(load_target):
    program = load_target()
    got = program.build_chain(["go", "team", "go", "team"])
    assert got.get("go") == ["team", "team"], \
        "Keep repeats: 'team' came after 'go' twice, so it should be in the list twice."


def test_story_only_uses_pairs_from_the_text(load_target):
    program = load_target()
    words = program.words_of(program.TEXT)
    pairs = set(zip(words, words[1:]))
    chain = program.build_chain(words)
    random.seed(1)
    story = program.generate(chain, "the", 20).split()
    assert len(story) > 1, "The story should have more than one word."
    bad = [pair for pair in zip(story, story[1:]) if pair not in pairs]
    assert not bad, f"Every word in the story should follow a word it really followed in the text. These did not: {bad}"


def test_same_seed_same_story(load_target):
    program = load_target()
    chain = program.build_chain(program.words_of(program.TEXT))
    random.seed(42)
    first = program.generate(chain, "the", 12)
    random.seed(42)
    second = program.generate(chain, "the", 12)
    assert first == second, "With the same random seed the story should come out the same."
