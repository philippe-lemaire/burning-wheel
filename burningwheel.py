import random
import numpy as np


def roll(
    shade="black", dice=0, obstacle=None, open_ended=False, luck=False, last_roll=None
):
    """Rolls a Burning wheel test. Prints the outcome in plain English and returns a list of dice face values.
    Use the returned list as last_roll argument with luck=True to reroll with the Luck rule of artha spending"""
    # shade setting
    if shade.lower().startswith("b"):
        threshold = 4
    elif shade.lower().startswith("g"):
        threshold = 3
    elif shade.lower().startswith("w"):
        threshold = 2
    else:
        raise ValueError(
            "Shade must be a string such as 'b', 'black', 'grey', 'G', or 'white', 'w'"
        )

    # if luck, it's a reroll for exploding 6s
    if luck:
        rolls = last_roll
    else:
        rolls = [random.randint(1, 6) for die in range(dice)]

    # if the test is naturally open ended, or if it's a luck reroll
    if open_ended or luck:
        to_explode = rolls.count(6)
        # explode 6s
        while to_explode > 0:
            print("explosion")
            new_rolls = [random.randint(1, 6) for die in range(to_explode)]
            to_explode = new_rolls.count(6)
            rolls.extend(new_rolls)

    # Print the dice results
    print(f"You rolled: {rolls}.")
    successes = len([die for die in rolls if die >= threshold])

    if obstacle:
        if successes < obstacle:
            result = f"You failed to meet the obstacle. The obstacle was {obstacle} and you got {successes} successes."

        elif successes == obstacle:
            result = f"You met the obstacle. The obstacle was {obstacle} and you got {successes} successes."

        else:
            result = f"You beat the obstacle. The obstacle was {obstacle} and you got {successes} successes. Your margin of success is {successes-obstacle}."

    else:
        result = f"You got {successes} successes."

    return rolls, result


def assess_difficulty(dice, obstacle):
    """Prints out the difficulty of the test to log for advancement based on the dice rolled and the obstacle.
    Dice granted by artha spending do not count in the dice total.
    Example use:
    assess_difficulty(dice=5, obstacle=5)
    Prints: '5 dice for an Ob5: this is a difficult test.'
    """

    # table is the obstacle / dice difficulty found in the book as a 2D np.array
    # 0s are routine, 1s are difficult and 2s are challenging

    table = np.zeros((12, 13), dtype="int32")
    table[0, 1:] = 2  # at 1 die everything above ob 1 is difficult
    # 2 dice
    table[1, 1] = 1
    table[1, 2:] = 2
    # 3 dice
    table[2, 2] = 1
    table[2, 3:] = 2
    # 4 dice
    table[3, 2:4] = 1
    table[3, 4:] = 2
    # 5 dice
    table[4, 3:5] = 1
    table[4, 5:] = 2
    # 6 dice
    table[5, 4:6] = 1
    table[5, 6:] = 2
    # 7 dice
    table[6, 4:7] = 1
    table[6, 7:] = 2
    # 8 dice
    table[7, 5:8] = 1
    table[7, 8:] = 2
    # 9 dice
    table[8, 6:9] = 1
    table[8, 9:] = 2
    # 10 dice
    table[9, 7:10] = 1
    table[9, 10:] = 2
    # 11 dice
    table[10, 8:11] = 1
    table[10, 11:] = 2
    # 12 dice
    table[11, 9:12] = 1
    table[11, 12:] = 2

    if obstacle > 13:
        obstacle = 13
    if dice > 12:
        return "This function can not assess tests passed with more than 12 dice."

    difficulty = table[dice - 1, obstacle - 1]

    if difficulty == 0:
        return f"{dice} dice for an Ob{obstacle}: this is a routine test."
    if difficulty == 1:
        return f"{dice} dice for an Ob{obstacle}: this is a difficult test."
    if difficulty == 2:
        return f"{dice} dice for an Ob{obstacle}: this is a challenging test."

    return None
