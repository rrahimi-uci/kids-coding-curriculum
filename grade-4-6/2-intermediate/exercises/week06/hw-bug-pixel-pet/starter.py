# Homework Bug Hunt: Pixel Pet
# A virtual pet stored in a dictionary. There are THREE bugs.
# Press Run and read the traceback bottom-up to find the first one.


def make_pet(name):
    """Return a new pet. Hunger and happiness go from 0 to 10."""
    return {"name": name, "hunger": 5, "happiness": 5}


def feed(pet):
    """Feeding makes the pet less hungry (but never below 0)."""
    pet["Hunger"] = pet["hunger"] - 3
    if pet["hunger"] < 0:
        pet["hunger"] = 0
    return pet


def play(pet):
    """Playing makes the pet happier and a little hungrier."""
    pet["happiness"] = pet["happiness"] + 2
    pet["hunger"] = pet["hungry"] + 1
    return pet


def mood(pet):
    """Return "grumpy" if the pet is very hungry OR very unhappy, else "happy"."""
    if pet["hunger"] >= 8 and pet["happiness"] <= 2:
        return "grumpy"
    return "happy"


if __name__ == "__main__":
    pet = make_pet("Pixel")
    play(pet)
    play(pet)
    feed(pet)
    print(pet)
    print(f"{pet['name']} feels {mood(pet)}.")
    # A second pet checks the mood rules. Biscuit is very hungry (9).
    biscuit = {"name": "Biscuit", "hunger": 9, "happiness": 6}
    print(f"{biscuit['name']} feels {mood(biscuit)}.")
