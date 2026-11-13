# TEACHER REFERENCE SOLUTION: Exercise 7.1 - Recursion warm-up
#
# What the program does: counts down from 5 to "Liftoff!", adds up the
# numbers 1 to 10 (55), and spells "recursion" backwards ("noisrucer").
# Key idea: recursion, a function that calls ITSELF on a smaller version of
# the same problem until the problem is so small it can be answered at once.
# Approach: every function has a BASE CASE (the tiny problem answered at
# once, which stops the chain) and a RECURSIVE CASE (do one small step, then
# let the function handle the rest). The base case is what stops it from
# calling itself forever.


def countdown(n):
    """Print n, n-1, ... 1 and then Liftoff!"""
    if n <= 0:                # base case: nothing left to count
        print("Liftoff!")
        return
    print(n)                  # one small step...
    countdown(n - 1)          # ...then the same job on a smaller number


def sum_to(n):
    """Return 1 + 2 + ... + n, worked out by recursion."""
    # Base case: adding up no numbers gives 0. Using "<= 0" (not "== 0")
    # also keeps a negative n from counting down forever.
    if n <= 0:
        return 0
    # Recursive case: n plus "the sum of everything below n". Each call waits
    # for the smaller call to answer, then adds its own n on the way back.
    return n + sum_to(n - 1)


def reverse(word):
    """Return the word backwards, e.g. 'turtle' -> 'eltrut'."""
    # Base case: an empty word or a single letter reads the same backwards.
    if len(word) <= 1:
        return word
    # Recursive case: the last letter goes first, then the reverse of all
    # the letters before it (word[:-1] means "everything except the last").
    return word[-1] + reverse(word[:-1])


if __name__ == "__main__":
    countdown(5)
    print("sum_to(10) =", sum_to(10))
    print("reverse('recursion') =", reverse("recursion"))


# Common mistakes children make here:
#   - Forgetting the base case (or never getting closer to it), so Python
#     stops with "RecursionError: maximum recursion depth exceeded".
#   - Writing sum_to(n) + sum_to(n - 1) or calling sum_to(n) instead of
#     sum_to(n - 1), which never gets smaller.
#   - In reverse, putting the letters in the wrong order:
#     reverse(word[:-1]) + word[-1] gives the word back unchanged.
#
# Another correct way: use a loop (no recursion) or a slice.
#   sum_to:  return n * (n + 1) // 2
#   reverse: return word[::-1]
