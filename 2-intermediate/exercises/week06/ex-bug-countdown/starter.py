# Bug Hunt Station 3: Rocket Countdown
# Press Run. The rocket never launches! After a moment you get a
# RuntimeError from the safety net. Make a trace table on paper:
#
#   round | n | numbers
#   ------+---+-----------
#     1   | 5 | [5]
#     2   |   |
#
# What should change each time through the loop... but does not?


def countdown(start):
    """Return a list counting down from start to 1, e.g. [3, 2, 1]."""
    numbers = []
    n = start
    rounds = 0
    while n > 0:
        numbers.append(n)
        rounds = rounds + 1
        if rounds > 1000:                  # safety net: you do not need to change this
            raise RuntimeError("The loop ran more than 1000 times. It looks stuck! Does n get smaller?")
    return numbers


def launch(start):
    """Print the countdown, then lift off."""
    for number in countdown(start):
        print(f"{number}...")
    print("LIFT OFF!")


if __name__ == "__main__":
    launch(5)
