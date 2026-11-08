"""Checks for Exercise 2.1 - Pet Class."""


def test_each_pet_has_its_own_numbers(load_target):
    pets = load_target()
    pip = pets.Pet("Pip", "dragon")
    bo = pets.Pet("Bo", "robot cat")
    pip.feed()
    pip.play()
    assert (bo.hunger, bo.happiness) == (5, 5), "Changing Pip must not change Bo: each object keeps its own attributes."
    assert pip.name == "Pip" and bo.species == "robot cat", "Each pet should remember its own name and species."


def test_play_makes_happier_and_hungrier(load_target):
    pets = load_target()
    pet = pets.Pet("Pip", "dragon")
    pet.play()
    assert pet.happiness == 7, f"After one play, happiness should go from 5 to 7, not {pet.happiness}."
    assert pet.hunger == 6, f"After one play, hunger should go from 5 to 6, not {pet.hunger}."


def test_numbers_stay_between_0_and_10(load_target):
    pets = load_target()
    pet = pets.Pet("Pip", "dragon")
    for _ in range(10):
        pet.play()
    assert pet.happiness == 10, f"Happiness should stop at 10, but it is {pet.happiness}."
    assert pet.hunger == 10, f"Hunger should stop at 10, but it is {pet.hunger}."
    for _ in range(10):
        pet.feed()
    assert pet.hunger == 0, f"Hunger should stop at 0, but it is {pet.hunger}."


def test_mood(load_target):
    pets = load_target()
    pet = pets.Pet("Pip", "dragon")
    cases = [(8, 9, "hungry"), (2, 9, "happy"), (2, 1, "bored"), (5, 5, "okay")]
    for hunger, happiness, expected in cases:
        pet.hunger, pet.happiness = hunger, happiness
        assert pet.mood() == expected, (
            f"With hunger {hunger} and happiness {happiness}, mood() should be {expected!r}, not {pet.mood()!r}."
        )


def test_describe(load_target):
    pets = load_target()
    pet = pets.Pet("Pip", "dragon")
    text = pet.describe()
    assert "Pip" in text and "dragon" in text and "okay" in text, (
        f"describe() should mention the name, species and mood, like 'Pip the dragon feels okay.' Got {text!r}"
    )
