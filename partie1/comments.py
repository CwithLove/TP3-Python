
import random


def get_comment(score):
    if score >= 900:
        rank = "S - Dog Whisperer"
        comments = [
            "WOW! Are you secretly a dog?",
            "100% certified dog whisperer!",
            "Impressive! Even the dogs are jealous.",
            "Do you bark in your sleep?",
            "Absolute legend. Woof woof!"
        ]

    elif score >= 700:
        rank = "A - Dog Expert"
        comments = [
            "Nice! The dogs approve.",
            "Impressive! You know your dogs.",
            "Almost perfect. Almost...",
            "The Dog Council respects you.",
            "You're one good human!"
        ]

    elif score >= 500:
        rank = "B - Good Boy"
        comments = [
            "Not bad, human. Not bad.",
            "Good job! Have a treat.",
            "Half dog expert, half confused human.",
            "You're getting there, buddy!",
            "The dogs are mildly impressed."
        ]

    elif score >= 300:
        rank = "C - Puppy Trainee"
        comments = [
            "You've got some learning to do, buddy.",
            "Is that a Husky or a potato?",
            "At least you tried!",
            "The dogs are judging you.",
            "Maybe ask a dog for help next time?"
        ]

    else:
        rank = "D - Cat Person"
        comments = [
            "You're not too lucky today, huh?",
            "Are you sure you like dogs?",
            "Maybe cats are more your thing.",
            "Even the Chihuahua is disappointed.",
            "Well... that was something."
        ]

    return rank, random.choice(comments)
