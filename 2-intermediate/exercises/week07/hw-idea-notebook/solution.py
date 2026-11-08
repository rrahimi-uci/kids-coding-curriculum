# TEACHER REFERENCE SOLUTION: Homework 7 - Game Idea Notebook
#
# What it does: a tiny notebook that remembers game and art ideas in a text
# file (game_ideas.txt), so they are still there the next time you run it.
# The menu lets you add an idea (a), list the ideas (l) or quit (q).
# Key ideas: appending a line to a file, reading it back, and try / except
# to cope with a file that does not exist yet.
# Approach: add_idea() appends the idea plus a new line. load_ideas() reads
# every non-empty line, and creates an empty file if there is none yet.
# Ideas only: never save personal information (real names, addresses...).

IDEA_FILE = "game_ideas.txt"


def add_idea(filename, idea):
    """Add one idea as a new line at the end of the file."""
    # "a" (append) adds to the end, so older ideas are kept. "w" would wipe them.
    with open(filename, "a") as file:
        file.write(idea + "\n")      # "\n" starts a new line for the next idea


def load_ideas(filename):
    """Return a list of ideas (one per line, no empty lines).
    If the file is missing, make an empty one and return []."""
    ideas = []
    try:
        with open(filename, "r") as file:
            for line in file:
                idea = line.strip()          # remove the "\n" at the end
                if idea != "":               # skip empty lines
                    ideas.append(idea)
    except FileNotFoundError:
        # First run ever: there is no file to read yet. Make an empty one so
        # the notebook starts cleanly instead of crashing. "w" is safe here
        # because there is nothing to wipe.
        with open(filename, "w") as file:
            file.write("")
    return ideas


def show_ideas(ideas):
    """Print the ideas as a numbered list."""
    if len(ideas) == 0:
        print("No ideas yet. Type a to add one!")
    for number in range(len(ideas)):
        # Lists count from 0, but people count from 1, so we add 1.
        print(f"{number + 1}. {ideas[number]}")


if __name__ == "__main__":
    print("=== My Game Idea Notebook ===")
    while True:
        choice = input("a = add an idea, l = list ideas, q = quit: ").strip().lower()
        if choice == "a":
            idea = input("Your idea: ").strip()
            if idea != "":
                add_idea(IDEA_FILE, idea)
                print("Saved!")
        elif choice == "l":
            show_ideas(load_ideas(IDEA_FILE))
        elif choice == "q":
            print("Bye! Your ideas are safe in", IDEA_FILE)
            break
        else:
            print("Please type a, l or q.")


# Common mistakes children make here:
# - Using "w" in add_idea(): the notebook only ever remembers the newest idea.
# - Forgetting "\n": the ideas are glued together on one long line.
# - Forgetting strip() when reading: every idea keeps its "\n" and the list
#   shows stray blank lines (and the tests fail).
# - Forgetting the except branch: the very first run crashes with a
#   FileNotFoundError.
#
# Another correct way: read the whole file at once with splitlines():
#     with open(filename, "r") as file:
#         ideas = [line.strip() for line in file.read().splitlines() if line.strip()]
