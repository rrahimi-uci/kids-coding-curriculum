# Commit Coach - reference solution
# A helper that checks commit messages and spots secrets before you commit.
# Level 2 review: functions with return, lists, for loops and if/elif/else.

# Messages that do not tell future-you anything useful.
BORING_MESSAGES = ["stuff", "update", "changes", "fix", "asdf", "wip", "misc", "work"]

# Words that often mean "this line holds a secret". Secrets never go in git!
SECRET_WORDS = ["password", "passwd", "secret", "api_key", "token"]

MAX_LENGTH = 50


def is_good_message(message):
    """Return True if the commit message would help future-you."""
    text = message.strip()
    if text == "":
        return False
    if len(text) > MAX_LENGTH:
        return False
    if text.lower() in BORING_MESSAGES:
        return False
    if len(text.split()) < 2:
        return False
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
    return verb.strip().capitalize() + " " + thing.strip()


def find_secrets(lines):
    """Return a list of the lines that look like they hold a secret."""
    found = []
    for line in lines:
        lower = line.lower()
        for word in SECRET_WORDS:
            if word in lower:
                found.append(line)
                break  # one secret word is enough - do not add the line twice
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
