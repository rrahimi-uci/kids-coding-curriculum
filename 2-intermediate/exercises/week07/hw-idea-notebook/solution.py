# Game Idea Notebook - reference solution
# A tiny notebook that remembers your game and art ideas in a file.
# Ideas only: never save personal information (real names, addresses...).

IDEA_FILE = "game_ideas.txt"


def add_idea(filename, idea):
    """Add one idea as a new line at the end of the file."""
    with open(filename, "a") as file:
        file.write(idea + "\n")


def load_ideas(filename):
    """Return a list of ideas (one per line, no empty lines).
    If the file is missing, make an empty one and return []."""
    ideas = []
    try:
        with open(filename, "r") as file:
            for line in file:
                idea = line.strip()
                if idea != "":
                    ideas.append(idea)
    except FileNotFoundError:
        with open(filename, "w") as file:
            file.write("")
    return ideas


def show_ideas(ideas):
    """Print the ideas as a numbered list."""
    if len(ideas) == 0:
        print("No ideas yet. Type a to add one!")
    for number in range(len(ideas)):
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
