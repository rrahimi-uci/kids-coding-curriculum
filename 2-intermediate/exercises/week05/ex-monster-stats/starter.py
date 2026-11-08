# Monster Stats
# A monster is stored in a dictionary: keys (names) and values.


def make_monster(name):
    """Return a new level-1 monster as a dictionary."""
    return {"name": name, "level": 1, "health": 30, "attack": 4, "speed": 2}


def stat_report(monster):
    """Return a list of lines like "health: 30", one for every key."""
    lines = []
    # TODO 1: for key, value in monster.items():
    #             append an f-string like "health: 30" to lines
    return lines


def level_up(monster):
    """Make the monster stronger: +1 level, +10 health, +2 attack. Return it."""
    monster["level"] = monster["level"] + 1
    # TODO 2: add 10 to health and 2 to attack, the same way.
    return monster


def get_stat(monster, stat):
    """Return the value of a stat, or 0 if the monster does not have it."""
    # TODO 3 (bug hunt): looking up a key that is not there crashes with KeyError.
    # Check first:  if stat in monster:
    return monster[stat]


if __name__ == "__main__":
    blobby = make_monster("Blobby")
    blobby["color"] = "bluish green"      # adding a new key is easy
    for line in stat_report(blobby):
        print(line)
    print("Blobby eats a glowing mushroom... LEVEL UP!")
    level_up(blobby)
    for line in stat_report(blobby):
        print(line)
    stat = input("Which stat do you want to look up? ")
    print(f"{stat}: {get_stat(blobby, stat)}")
