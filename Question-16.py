# Q16: Number Guessing Game
# This program lets the user guess a randomly generated number.

import random

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0  # To count number of tries

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!")

while True:
    try:
        # Taking user guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check guess
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")

        elif guess < secret_number:
            print("Too Low! Try again.")

        elif guess > secret_number:
            print("Too High! Try again.")

        else:
            # Correct guess
            print("\nCongratulations! You guessed correctly.")
            print("Secret Number:", secret_number)
            print("Attempts Taken:", attempts)
            break

    except:
        print("Please enter a valid integer.")