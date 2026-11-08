# Monster Stats - reference solution
# A dictionary stores values under names (keys), like a labeled
# character sheet. monster["health"] looks up the value for "health".


def make_monster(name):
    """Return a new level-1 monster as a dictionary."""
    return {"name": name, "level": 1, "health": 30, "attack": 4, "speed": 2}


def stat_report(monster):
    """Return a list of lines like "health: 30", one for every key."""
    lines = []
    for key, value in monster.items():
        lines.append(f"{key}: {value}")
    return lines


def level_up(monster):
    """Make the monster stronger: +1 level, +10 health, +2 attack. Return it."""
    monster["level"] = monster["level"] + 1
    monster["health"] = monster["health"] + 10
    monster["attack"] = monster["attack"] + 2
    return monster


def get_stat(monster, stat):
    """Return the value of a stat, or 0 if the monster does not have it."""
    if stat in monster:
        return monster[stat]
    return 0


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
