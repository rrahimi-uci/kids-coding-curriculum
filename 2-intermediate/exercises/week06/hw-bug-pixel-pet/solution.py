# TEACHER REFERENCE SOLUTION: Homework 6 - Pixel Pet (bug hunt)
#
# What it does: keeps a virtual pet in a dictionary. Feeding lowers hunger,
# playing raises happiness (and hunger a little), and mood() says whether the
# pet is "grumpy" or "happy".
# Key ideas: dictionary keys must be spelled exactly (capital letters count),
# and "or" versus "and" in a condition.
# Approach: three fixes - two wrong key names (one crashes, one silently
# creates a stray key) and one wrong logic word in mood().


def make_pet(name):
    """Return a new pet. Hunger and happiness go from 0 to 10."""
    return {"name": name, "hunger": 5, "happiness": 5}


def feed(pet):
    """Feeding makes the pet less hungry (but never below 0)."""
    # FIX 1: the starter wrote to pet["Hunger"] (capital H). That is a
    # different key, so Python quietly added a new one and "hunger" never
    # went down. Keys must match exactly.
    pet["hunger"] = pet["hunger"] - 3
    if pet["hunger"] < 0:
        pet["hunger"] = 0             # hunger never goes below 0
    return pet


def play(pet):
    """Playing makes the pet happier and a little hungrier."""
    pet["happiness"] = pet["happiness"] + 2
    # FIX 2: the starter read pet["hungry"], a key that does not exist, which
    # crashed with a KeyError. The real key is "hunger".
    pet["hunger"] = pet["hunger"] + 1
    return pet


def mood(pet):
    """Return "grumpy" if the pet is very hungry OR very unhappy, else "happy"."""
    # FIX 3: the starter used "and", so the pet was only grumpy when BOTH
    # problems happened together. The rule says either one is enough: "or".
    if pet["hunger"] >= 8 or pet["happiness"] <= 2:
        return "grumpy"
    return "happy"


if __name__ == "__main__":
    pet = make_pet("Pixel")
    play(pet)
    play(pet)
    feed(pet)
    print(pet)
    print(f"{pet['name']} feels {mood(pet)}.")


# Common mistakes children make here:
# - Fixing the capital letter in feed() by changing the key in make_pet
#   instead (to "Hunger"), which then breaks play() and mood().
# - Fixing the KeyError by adding a "hungry" key to make_pet, instead of
#   correcting the spelling in play().
# - Changing the numbers in mood() (8 and 2) instead of the word "and".
#   The numbers match the rules; the logic word was wrong.
#
# Another correct way: feed() can use max() so the "below 0" check is one line:
#     pet["hunger"] = max(0, pet["hunger"] - 3)
