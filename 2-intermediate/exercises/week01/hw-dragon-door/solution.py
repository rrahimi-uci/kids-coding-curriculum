# Dragon Door - reference solution
# The dragon door opens if you have the golden key AND you are level 3 or
# more, OR if you are level 10 or more (legends do not need keys).


def door_opens(has_key, level):
    """Return True if the dragon door opens, otherwise False."""
    if (has_key and level >= 3) or level >= 10:
        return True
    else:
        return False


if __name__ == "__main__":
    hero = input("Hero name (make one up): ")
    key_answer = input("Do you have the golden key? (yes/no) ")
    has_key = key_answer.lower() == "yes"
    level = int(input("What level are you? "))
    if door_opens(has_key, level):
        print(f"The dragon door creaks open. Welcome, {hero}!")
    else:
        print(f"The door stays shut, {hero}. Find the key or reach level 10.")
