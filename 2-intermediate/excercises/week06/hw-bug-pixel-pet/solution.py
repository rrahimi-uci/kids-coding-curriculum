# Homework Bug Hunt: Pixel Pet - FIXED version (teacher)
# Bug 1: play() looked up the key "hungry" (no such key) -> KeyError.
# Bug 2: feed() changed the key "Hunger" with a capital H. Keys must match
#        exactly, so it made a NEW key instead of changing "hunger".
# Bug 3: mood() used "and" where the rule says "or", so the pet was only
#        grumpy when it was hungry AND unhappy at the same time.


def make_pet(name):
    """Return a new pet. Hunger and happiness go from 0 to 10."""
    return {"name": name, "hunger": 5, "happiness": 5}


def feed(pet):
    """Feeding makes the pet less hungry (but never below 0)."""
    pet["hunger"] = pet["hunger"] - 3
    if pet["hunger"] < 0:
        pet["hunger"] = 0
    return pet


def play(pet):
    """Playing makes the pet happier and a little hungrier."""
    pet["happiness"] = pet["happiness"] + 2
    pet["hunger"] = pet["hunger"] + 1
    return pet


def mood(pet):
    """Return "grumpy" if the pet is very hungry OR very unhappy, else "happy"."""
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
