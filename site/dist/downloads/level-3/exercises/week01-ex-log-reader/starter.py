# Log Reader - YOUR version
# Reads the text that "git log --oneline" prints. Each line looks like:
#     9c1e2d4 Add high score file
# The first word is the commit id (a short "hash"); the rest is the message.
# Finish the TODOs, then press Run and see if it does what the README says.

SAMPLE_LOG = """9c1e2d4 Add high score file
5b7a913 Fix hero walking through walls
2d4f6a8 Add jump to hero
a1b2c3d Draw first level
0f9e8d7 Start game project
"""


def parse_line(line):
    """Split one log line into a tuple (commit_id, message). (Already done!)"""
    parts = line.strip().split(" ", 1)  # split only at the FIRST space
    commit_id = parts[0]
    if len(parts) > 1:
        message = parts[1]
    else:
        message = ""
    return (commit_id, message)


def parse_log(text):
    """Turn the whole log text into a list of (commit_id, message) tuples."""
    commits = []
    # TODO 1: loop over text.splitlines(). For every line that is not empty,
    #         append parse_line(line) to commits.
    return commits


def count_commits(text):
    """How many save points are in the log?"""
    # TODO 2: use parse_log and len
    return 0


def find_commits(text, word):
    """Return the ids of commits whose message contains word (any capitals)."""
    ids = []
    # TODO 3: loop over parse_log(text). If word.lower() is in message.lower(),
    #         append the commit id to ids.
    return ids


def oldest_first(text):
    """git log shows the NEWEST commit first. Return the messages oldest first."""
    messages = []
    # TODO 4: collect every message, then reverse the list
    return messages


if __name__ == "__main__":
    print(f"This project has {count_commits(SAMPLE_LOG)} commits.")
    print("The story of the project, from the beginning:")
    for number, message in enumerate(oldest_first(SAMPLE_LOG), start=1):
        print(f"  {number}. {message}")
    print("Commits about the hero:", find_commits(SAMPLE_LOG, "hero"))
