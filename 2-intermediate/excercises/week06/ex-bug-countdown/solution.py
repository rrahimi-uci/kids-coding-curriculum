# Bug Hunt Station 3: Rocket Countdown - FIXED version (teacher)
# Bug: n never changed inside the while loop, so "n > 0" stayed True for
# ever (an infinite loop). Fix: n = n - 1 inside the loop.
# The safety net stops a stuck loop after 1000 rounds with a clear message.


def countdown(start):
    """Return a list counting down from start to 1, e.g. [3, 2, 1]."""
    numbers = []
    n = start
    rounds = 0
    while n > 0:
        numbers.append(n)
        n = n - 1
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
