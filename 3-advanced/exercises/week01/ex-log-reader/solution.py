"""TEACHER REFERENCE SOLUTION: Log Reader

What the program does: it reads the text that `git log --oneline` prints (one line per saved
version of a project: a short id, then the message) and turns it into data Python can use. It
counts the commits, finds the ones about a word, and lists the messages oldest first.

Key ideas practiced: `splitlines()`, tuples like (id, message), looping over a list of
tuples, reusing one function inside others, and reversing a list.

Approach: `parse_log` does the hard work once (one tuple per non-empty line). The other three
functions all start from `parse_log`, so none of them needs to know how a log line looks.
"""

SAMPLE_LOG = """9c1e2d4 Add high score file
5b7a913 Fix hero walking through walls
2d4f6a8 Add jump to hero
a1b2c3d Draw first level
0f9e8d7 Start game project
"""


def parse_line(line):
    """Split one log line into a tuple (commit_id, message)."""
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
    # Step 1: splitlines() gives one string per line of the log.
    for line in text.splitlines():
        # Blank lines would turn into empty commits, so skip them.
        if line.strip() != "":
            commits.append(parse_line(line))
    return commits


def count_commits(text):
    """How many save points are in the log?"""
    # Step 2: one tuple per commit, so the length of the list is the number of commits.
    return len(parse_log(text))


def find_commits(text, word):
    """Return the ids of commits whose message contains word (any capitals)."""
    ids = []
    # Step 3: each tuple is unpacked into two names, so we can use id and message directly.
    for commit_id, message in parse_log(text):
        # Lowercase BOTH sides so "HERO" finds "hero" and "Hero".
        if word.lower() in message.lower():
            ids.append(commit_id)
    return ids


def oldest_first(text):
    """git log shows the NEWEST commit first. Return the messages oldest first."""
    messages = []
    # Step 4: collect the messages in log order (newest first) ...
    for commit_id, message in parse_log(text):  # commit_id is not needed here
        messages.append(message)
    # ... then flip the list so the first commit ever made comes first.
    messages.reverse()
    return messages


if __name__ == "__main__":
    print(f"This project has {count_commits(SAMPLE_LOG)} commits.")
    print("The story of the project, from the beginning:")
    for number, message in enumerate(oldest_first(SAMPLE_LOG), start=1):
        print(f"  {number}. {message}")
    print("Commits about the hero:", find_commits(SAMPLE_LOG, "hero"))


# Common mistakes children make here:
# - Forgetting to skip empty lines, so the blank line at the end becomes a fake commit
#   (count is one too big).
# - Comparing `word in message` without `.lower()`, so "HERO" finds nothing.
# - Writing `messages = messages.reverse()`: reverse() changes the list in place and returns
#   None, so the answer becomes None. Use `messages.reverse()` alone or `messages[::-1]`.
# - Using `print` instead of `return`.
#
# Another correct way for oldest_first (one line, using a slice to reverse):
#     return [message for commit_id, message in parse_log(text)][::-1]
