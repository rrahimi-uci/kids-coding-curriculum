# TEACHER REFERENCE SOLUTION: Monster Stats (Exercise 5.1)
#
# What the program does: it stores a game monster as a dictionary (a character
# sheet of labels and values), prints its stats, levels it up, prints the stats
# again, and looks up a stat the player types in.
# Key ideas practiced: dictionaries (keys and values), looping with .items(),
# changing a value, adding a new key, and checking "if stat in monster" before
# a lookup so a missing key does not crash the program.
# Approach: each function does one job on the dictionary. The bug hunt is
# get_stat(): looking up a key that is not there raises a KeyError, so we first
# ask whether the key exists and return 0 if it does not.


def make_monster(name):
    """Return a new level-1 monster as a dictionary."""
    return {"name": name, "level": 1, "health": 30, "attack": 4, "speed": 2}


def stat_report(monster):
    """Return a list of lines like "health: 30", one for every key."""
    lines = []
    # .items() gives us each key and its value together, one pair at a time.
    for key, value in monster.items():
        lines.append(f"{key}: {value}")
    return lines


def level_up(monster):
    """Make the monster stronger: +1 level, +10 health, +2 attack. Return it."""
    # We read the old value, add to it, and store it back under the same key.
    monster["level"] = monster["level"] + 1
    monster["health"] = monster["health"] + 10
    monster["attack"] = monster["attack"] + 2
    return monster


def get_stat(monster, stat):
    """Return the value of a stat, or 0 if the monster does not have it."""
    # FIX 1: monster[stat] crashed with KeyError when the stat (like "magic") was
    # not in the dictionary. Checking with "in" first makes a missing stat safe.
    if stat in monster:
        return monster[stat]
    return 0


if __name__ == "__main__":
    blobby = make_monster("Blobby")
    blobby["color"] = "bluish green"      # assigning to a new key adds it to the dictionary
    for line in stat_report(blobby):
        print(line)
    print("Blobby eats a glowing mushroom... LEVEL UP!")
    level_up(blobby)
    for line in stat_report(blobby):
        print(line)
    stat = input("Which stat do you want to look up? ")
    print(f"{stat}: {get_stat(blobby, stat)}")


# Common mistakes children make here:
# - Using a number instead of a key (monster[0]); dictionaries are looked up by
#   their key names, such as monster["health"].
# - Forgetting the quotes: monster[health] looks for a variable called health,
#   instead of the key "health".
# - Forgetting the f in the f-string, so the report prints {key}: {value} literally.
# - Writing monster["health"] + 10 without assigning it back, so nothing changes.
#
# Another correct way: the dictionary method get() does the "check first" for us.
#   return monster.get(stat, 0)
# And += is a short way to add to a value:
#   monster["health"] += 10
