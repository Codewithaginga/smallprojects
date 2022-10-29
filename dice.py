# import random
# define a function to roll
# create a dictionary

import random

def roll_dice():

    roll = input('Roll dice (yes/No): ')

    while roll.lower() == "Yes".lower():

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f'dice rolled: {dice1} {dice2}')

        roll = input(f'Roll again? (Yes/No): ')


roll_dice()