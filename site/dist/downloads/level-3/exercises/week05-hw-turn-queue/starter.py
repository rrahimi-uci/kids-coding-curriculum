# Turn Queue - YOUR version
# A queue is first in, first out - like a line at the lunch counter.
# collections.deque is Python's fast queue: append() joins at the back,
# popleft() takes from the front.
# Finish the TODOs, then press Run and see if it does what the README says.

from collections import deque


def make_queue(nicknames):
    """Return a deque holding the nicknames in order. (Already done!)"""
    return deque(nicknames)


def take_turn(queue):
    """The player at the front takes a turn, then goes to the back.
    Return their nickname (None if nobody is in the queue)."""
    if len(queue) == 0:
        return None
    # TODO 1: player = queue.popleft(), then queue.append(player), then return player
    return None


def leave(queue, nickname):
    """Remove a player who has to leave. Return True if they were in the queue."""
    # TODO 2: if nickname is in queue: queue.remove(nickname) and return True
    return False


def play_rounds(nicknames, turns):
    """Return the list of who plays, turn by turn. (Already done!)"""
    queue = make_queue(nicknames)
    order = []
    for _ in range(turns):
        order.append(take_turn(queue))
    return order


if __name__ == "__main__":
    players = ["Priya", "Sam", "Kai", "Zoe"]
    print("Turn order for 6 turns:", play_rounds(players, 6))
    line = make_queue(players)
    take_turn(line)
    leave(line, "Kai")
    print("Kai went home. Queue now:", list(line))
