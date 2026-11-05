
import random

secret_number = random.randint(1, 100)
attempts = 0

print("===== GUESS THE NUMBER =====")
print("I picked a number from 1 to 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the number!")
            print("Attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid whole number.")
