# Dice Rolling Simulator

# Imports
import random

# Dice Sets
dice_sets = {'D4': list(range(1, 5)), 
    'D6': list(range(1, 7)), 
    'D8': list(range(1, 9)), 
    'D10': list(range(1, 11)), 
    'D12': list(range(1, 13)), 
    'D20': list(range(1, 21)),
    'D100': list(range(1, 101))}

# Past Rolls
past_rolls = {'D4': [], 'D6': [], 'D8': [], 'D10': [], 'D12': [], 'D20': [], 'D100': []}

# Random Dice Roll
def dice_roll(dice_type):

    if dice_type == 'D100':

        roll = random.choice(dice_sets['D100'])
        past_rolls[dice_type].append(roll)

        return f"{roll}%"
    
    roll = random.choice(dice_sets[dice_type])
    past_rolls[dice_type].append(roll)

    return roll

# Choose Dice Type
def choose_dice():
    
    dice_type = input("Please choose the type of dice you want to roll (D4, D6, D8, D10, D12, D20, D100): ").upper()

    while dice_type not in ['D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']:
        dice_type = input("Please choose (D4, D6, D8, D10, D12, D20, D100): ").upper()

    return print(dice_roll(dice_type))

# Print Past dice rolls
def print_past_rolls():

    for key, value in past_rolls.items():

        if len(value) == 0:
            print(f"{key} has not been rolled yet.\n")
        
        elif key == 'D100':
            formatted_value = [f"{v}%" for v in value]
            print(f"{key}: [{', '.join(formatted_value)}]\n")
            print(f"You have rolled a {key} {len(value)} times.\n") 

        else:
            print(f"{key}: {value}\n")
            print(f"You have rolled a {key} {len(value)} times.\n")

# GAME LOOP

running = 'Y'
rolling = 'Y'

while running != 'N':

    running = input("Would you like to roll [Y /N]: ").upper()

    if running == 'Y':

        choose_dice()

        while rolling != 'N':

            rolling = input("Would you like to roll again [Y / N] or look at past rolls [P]: ").upper()

            if rolling == 'N':
                running = 'N'
                break

            if rolling == 'Y':
                choose_dice()

            if rolling == 'P':
                print_past_rolls()
    
    if running == 'N':
        print("Thank you for rolling!")
        break