"""TEACHER REFERENCE SOLUTION: Commit Coach

What the program does: it checks a git "commit message" (the short note you write when you
save a version of your project) and tells the child if the note is helpful. It can also build
a message from a verb and a thing, and it can spot lines of code that hold a secret such as a
password, so the child learns not to save secrets in git.

Key ideas practiced: functions that return a value, if checks, lists, for loops, and
text tools like strip(), lower(), split() and capitalize().

Approach: is_good_message turns each rule into one early return False; if no rule
catches the message, it is good. find_secrets loops over every line and over every secret
word, using break so a line is only added once.
"""

# Messages that do not tell future-you anything useful.
BORING_MESSAGES = ["stuff", "update", "changes", "fix", "asdf", "wip", "misc", "work"]

# Words that often mean "this line holds a secret". Secrets never go in git!
SECRET_WORDS = ["password", "passwd", "secret", "api_key", "token"]

MAX_LENGTH = 50


def is_good_message(message):
    """Return True if the commit message would help future-you."""
    # strip() removes spaces at both ends, so "   " counts as an empty message.
    text = message.strip()
    if text == "":
        return False
    # Step 1: too long to read in a list of commits.
    if len(text) > MAX_LENGTH:
        return False
    # Step 2: lower() makes "Update" and "update" the same, so capitals do not fool us.
    if text.lower() in BORING_MESSAGES:
        return False
    # Step 3: a good message says what AND to what ("Add jump"), so it needs 2+ words.
    # split() cuts the text at the spaces; len() then counts the pieces.
    if len(text.split()) < 2:
        return False
    # Every "bad" rule was checked and none matched, so the message is good.
    return True


def coach_tip(message):
    """Return one friendly tip about the message."""
    text = message.strip()
    if text == "":
        return "Write something! Say what you changed."
    if len(text) > MAX_LENGTH:
        return f"Shorter please: {MAX_LENGTH} characters or fewer (yours has {len(text)})."
    if not is_good_message(text):
        return "Be specific: say WHAT changed, like 'Add jump to hero'."
    return "Great message!"


def make_message(verb, thing):
    """Build a message like 'Add star shape' from a verb and a thing."""
    # Step 4: capitalize() makes only the first letter big. strip() cleans stray spaces.
    # The + signs glue the pieces together; the " " is the space in the middle.
    return verb.strip().capitalize() + " " + thing.strip()


def find_secrets(lines):
    """Return a list of the lines that look like they hold a secret."""
    found = []
    # Step 5: look at each line, and for each line try every secret word.
    for line in lines:
        # Make a lowercase copy to search in, so "API_KEY" matches "api_key".
        # We still append the ORIGINAL line, so the answer keeps its capitals.
        lower = line.lower()
        for word in SECRET_WORDS:
            if word in lower:
                found.append(line)
                break  # one secret word is enough - do not add the same line twice
    return found


if __name__ == "__main__":
    print("Commit Coach: type a commit message and get a tip.")
    print("Type q to quit.")
    while True:
        message = input("Message: ")
        if message.strip().lower() == "q":
            print("Happy committing!")
            break
        print(coach_tip(message))


# Common mistakes children make here:
# - Forgetting .lower() in find_secrets, so "API_KEY" is missed (the test hints at this).
# - Checking word in line for the wrong direction, or appending the line once per
#   matching word (without break) so a line shows up twice.
# - Using print instead of return: the function shows text but gives nothing back, so
#   the tests (and coach_tip) see None.
# - Forgetting that len(text) must be checked on the stripped text, not the raw message.
#
# Another correct way for find_secrets, using any() instead of an inner loop:
#     for line in lines:
#         if any(word in line.lower() for word in SECRET_WORDS):
#             found.append(line)
