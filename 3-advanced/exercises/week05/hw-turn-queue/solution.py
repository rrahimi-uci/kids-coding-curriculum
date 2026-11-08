"""TEACHER REFERENCE SOLUTION: Turn Queue

What the program does: it gives every player a fair turn in a game. The player at the front of
the line plays, then walks to the back of the line. A player who has to leave can be taken out
of the line. The sample run prints who plays during 6 turns, then shows the line after Kai
goes home.

Key ideas practiced: a queue (first in, first out), `collections.deque` with `append` and
`popleft`, and returning None or True/False to report what happened.

Approach: `popleft()` takes the front player, `append()` puts the same player at the back, so
the line rotates and everybody plays once before anybody plays twice. `leave` checks that the
player is really in the line before removing them.
"""

from collections import deque


def make_queue(nicknames):
    """Return a deque holding the nicknames in order."""
    return deque(nicknames)


def take_turn(queue):
    """The player at the front takes a turn, then goes to the back.
    Return their nickname (None if nobody is in the queue)."""
    # popleft() on an empty queue would crash, so answer None first.
    if len(queue) == 0:
        return None
    # Step 1: take from the FRONT, then add to the BACK, then report who played.
    player = queue.popleft()
    queue.append(player)
    return player


def leave(queue, nickname):
    """Remove a player who has to leave. Return True if they were in the queue."""
    # Step 2: remove() crashes if the name is not there, so look first with "in".
    if nickname in queue:
        queue.remove(nickname)
        return True
    return False


def play_rounds(nicknames, turns):
    """Return the list of who plays, turn by turn."""
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


# Common mistakes children make here:
# - Using `queue.pop()` (takes from the BACK) instead of `popleft()`, so the turn order is
#   backwards and the same player keeps playing.
# - Forgetting to `append` the player again, so players disappear after one turn.
# - Calling `queue.remove(nickname)` for someone who is not there (crash) or forgetting
#   `return True` / `return False`.
# - Forgetting to check for an empty queue in take_turn.
#
# Another correct way for take_turn (a deque can rotate itself):
#     player = queue[0]
#     queue.rotate(-1)   # moves the front player to the back
#     return player
