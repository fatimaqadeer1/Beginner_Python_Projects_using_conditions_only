"""1. Number Guessing Game
 Description: The program picks a random number between 1-100. You guess the number, and it
 tells you if your guess is too high or too low. You win when you guess it right.
 Concepts Used: input(), if-else, random
"""
import random
secret_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

# For testing only — show the secret number
# print(f"(Debug: The secret number is {secret_number})")

if guess > secret_number:
    print("Too high!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Congratulations! You guessed it right.")
