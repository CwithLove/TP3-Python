
import random


def generate_question(breeds):
    correct_breed = random.choice(breeds)

    wrong_breeds = [
        breed for breed in breeds
        if breed != correct_breed
    ]

    options = random.sample(wrong_breeds, 3)
    options.append(correct_breed)

    random.shuffle(options)

    return correct_breed, options
