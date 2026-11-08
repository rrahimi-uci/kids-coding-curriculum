"""Checks for Homework 5 - Turn Queue."""


def test_take_turn_goes_to_the_back(load_target):
    turns = load_target()
    queue = turns.make_queue(["Priya", "Sam", "Kai"])
    assert turns.take_turn(queue) == "Priya", "The player at the FRONT plays first."
    assert list(queue) == ["Sam", "Kai", "Priya"], f"After playing, Priya should go to the back. Queue: {list(queue)}"
    assert turns.take_turn(turns.make_queue([])) is None, "An empty queue has nobody to play: return None."


def test_play_rounds_takes_fair_turns(load_target):
    turns = load_target()
    order = turns.play_rounds(["Priya", "Sam", "Kai", "Zoe"], 6)
    assert order == ["Priya", "Sam", "Kai", "Zoe", "Priya", "Sam"], f"Everyone should get a turn before anyone goes twice. Got {order}"


def test_leave(load_target):
    turns = load_target()
    queue = turns.make_queue(["Priya", "Sam", "Kai"])
    assert turns.leave(queue, "Sam") is True, "Sam was in the queue, so leave should return True."
    assert list(queue) == ["Priya", "Kai"], f"After Sam leaves the queue should be Priya, Kai. Got {list(queue)}"
    assert turns.leave(queue, "Omar") is False, "Omar was never in the queue, so leave should return False."
