from random import randint
from logo import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
nivel_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number_exactly = randint(0, 100)

def number_guessing(endeavor):
    if endeavor > 0:
        print(f"You have {endeavor} attempts remaining to guess the number.")
        number = int(input("Make a guess: "))
        if number == number_exactly:
            return "You win"
        elif int(number) > number_exactly:
            print("Too high")
        else:
            print("Too low")

        endeavor -= 1
        result = number_guessing(endeavor)

        if result == "You win":
            return "You win"
    else:
        print(f"You've run out of guesses, you lose. The correct number was {number_exactly}.")

if nivel_difficulty == "hard":
    result = number_guessing(5)
    if result == "You win":
        print(f"You got it! The answer was {number_exactly}")
elif nivel_difficulty == "easy":
    result = number_guessing(10)
    if result == "You win":
        print(f"You got it! The answer was {number_exactly}")