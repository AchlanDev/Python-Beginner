# Number Guessing Game

# Imports
import random

def main():
    
    running = 'Y'

    while running != 'N':

        tries = 0
        guess = '0'

        print("Welcome to the Number Guessing Game!\n")

        print("There are three challenges to choose from:\n")

        print("1 - 10 | 1 - 50 | 1 - 100\n")

        challenge = input("Which challenge do you want to play [10, 50, 100]: \n")

        while challenge not in ('10', '50', '100') and challenge.isdigit():
            challenge = input("Please choose [10, 50, 100]: \n")

        challenge = int(challenge)

        challenge_number = random.choice(range(1, challenge + 1))

        while guess != challenge_number:

            guess = input(f"Take a guess [1 - {challenge}]: \n")

            guess = int(guess)

            while guess not in range(1, challenge + 1) and guess.is_integer():
                guess = input(f"Please choose a number between 1 and {challenge}: \n")
                guess = int(guess)

            

            if guess > challenge_number:
                print("Your guess is too high!\n")
                tries += 1

            if guess < challenge_number:
                print("Your guess is too low!\n")
                tries += 1

            if guess == challenge_number:
                print("Congratulations, you guessed correctly!\n")
                tries += 1
                print(f"You guessed correctly in {tries} tries!")
                break

        running = input("Would you like to play again [Y / N]: \n").upper()

        if running == 'N':
            print("Thank you for playing the Number Guessing Game! \n")
            break



if __name__ == "__main__":
    main()