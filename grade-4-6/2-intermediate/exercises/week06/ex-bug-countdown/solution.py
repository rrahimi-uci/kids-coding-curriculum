# TEACHER REFERENCE SOLUTION: Bug Hunt Station 3 - Rocket Countdown
#
# What it does: counts down from a starting number to 1, then prints
# "LIFT OFF!".
# Key ideas: a while loop only stops when its condition becomes False, so
# something INSIDE the loop must change the thing the condition looks at.
# Approach: the starter loop said "keep going while n is above 0" but never
# changed n, so n stayed 5 forever (an infinite loop). One line fixes it:
# make n one smaller every time through.


def countdown(start):
    """Return a list counting down from start to 1, e.g. [3, 2, 1]."""
    numbers = []
    n = start
    rounds = 0
    while n > 0:
        numbers.append(n)
        # FIX 1: n never got smaller, so "n > 0" was always True and the loop
        # never ended. Taking 1 away each round lets n reach 0 and stop.
        n = n - 1
        rounds = rounds + 1
        # Safety net (part of the starter, the child does not change it):
        # it stops a stuck loop with a clear message instead of freezing.
        if rounds > 1000:
            raise RuntimeError(
                "The loop ran more than 1000 times. It looks stuck! Does n get smaller?"
            )
    return numbers


def launch(start):
    """Print the countdown, then lift off."""
    for number in countdown(start):
        print(f"{number}...")
    print("LIFT OFF!")


if __name__ == "__main__":
    launch(5)


# Common mistakes children make here:
# - Fixing the wrong thing, e.g. changing "n > 0" to "n >= 0" or to
#   "n < 0". The condition was fine; the missing piece was a change to n.
# - Writing "n - 1" or "n == n - 1" on its own line. That works out a number
#   but never stores it. It has to be "n = n - 1".
# - Putting "n = n - 1" after the loop (not indented), so it is never reached.
# - Adding the line before "numbers.append(n)": the list then starts at 4
#   instead of 5.
#
# Another correct way: let Python do the counting with a for loop, so there
# is nothing to forget:
#     for n in range(start, 0, -1):
#         numbers.append(n)
