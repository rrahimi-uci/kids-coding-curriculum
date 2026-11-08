# Commit Coach - YOUR version
# A helper that checks commit messages and spots secrets before you commit.
# Finish the TODOs, then open check_my_work.py and press Run.

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
    # TODO 1: return False if text is longer than MAX_LENGTH
    # TODO 2: return False if text.lower() is in BORING_MESSAGES
    # TODO 3: return False if text has fewer than 2 words
    #         (hint: len(text.split()) counts the words)
    return True


def coach_tip(message):
    """Return one friendly tip about the message. (Already done!)"""
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
    # TODO 4: return the verb with a capital first letter, a space, then the thing.
    #         hint: "add".capitalize() gives "Add"
    return ""


def find_secrets(lines):
    """Return a list of the lines that look like they hold a secret."""
    found = []
    # TODO 5: loop over every line. If any word from SECRET_WORDS is inside
    #         line.lower(), append the line to found (only once per line).
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
