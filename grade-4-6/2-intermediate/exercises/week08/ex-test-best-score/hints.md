## Hint 1: Where to look
Read the top of `score_tools.py`. It lists what `best_score()` gives for a few lists, including an empty one. Your edge-case tests should check these places where a bug could hide.

## Hint 2: Try this
A test is only real if it has an `assert` line. The shape is `assert function(input) == expected_answer`. Pick a list, work out the answer yourself, and write it after `==`. Keep the message text short and clear.

## Hint 3: Almost there
Shapes to fill in: `assert best_score(____) == ____, "message"`. For the end test, put the biggest number in the last spot of the list. For your own test, try a list with `____` item, or a list where every number is the same.
