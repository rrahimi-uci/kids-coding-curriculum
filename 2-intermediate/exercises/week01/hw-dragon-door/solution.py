# TEACHER REFERENCE SOLUTION: Dragon Door (Homework 1)
#
# What the program does: it asks for a hero name, whether they have the golden
# key and their level, then says whether the dragon door opens.
# Key ideas practiced: combining "and" with "or" using brackets, and f-strings.
# Approach: the door opens in two separate ways, so we write each way as its own
# group: (key AND level 3 or more) OR (level 10 or more). The brackets keep the
# "and" group together so the "or" can then choose between the two ways.


def door_opens(has_key, level):
    """Return True if the dragon door opens, otherwise False."""
    # Way 1: you need BOTH the key and level 3. Way 2: legends (level 10+) need nothing.
    if (has_key and level >= 3) or level >= 10:
        return True
    else:
        return False


if __name__ == "__main__":
    hero = input("Hero name (make one up): ")
    key_answer = input("Do you have the golden key? (yes/no) ")
    has_key = key_answer.lower() == "yes"      # True only if the child typed yes
    level = int(input("What level are you? "))   # int() turns the text into a number
    if door_opens(has_key, level):
        print(f"The dragon door creaks open. Welcome, {hero}!")
    else:
        print(f"The door stays shut, {hero}. Find the key or reach level 10.")


# Common mistakes children make here:
# - Leaving out the brackets: "has_key and level >= 3 or level >= 10" happens to
#   work (Python does "and" before "or"), but brackets make the plan clear to read.
# - Writing "has_key and level >= 3 and level >= 10", which wrongly demands both.
# - Writing "level >= 3 or level >= 10": then anyone at level 3 gets in without a key.
# - Forgetting the f in front of the quotes, so {hero} is printed as plain text.
#
# Another correct way: an if statement is not needed, because the condition is
# already True or False, so the function can return it directly.
#   return (has_key and level >= 3) or level >= 10
