from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
    """Takes account data and returns printable format."""
    account_name = account["name"] # Search the name in the dict
    account_descr = account["description"] # Search the description in the dict
    account_country = account["country"] # Search the country in the dict
    return f"{account_name}, a {account_descr}, from {account_country}" # return name, description and country togheter

def check_answer(guess, a_followers, b_followers):
    """It takes the user's guess and counts the followers and returns if they get it right."""
    if a_followers > b_followers: # compare numbers count
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True

# Generating a random game_data account
account_b = random.choice(data)

# Make the game replayable
while game_should_continue:
    # Causing the account in position B to become the next account in position A
    account_a = account_b
    account_b = random.choice(data)

    # To avoid asking like comparisons
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask the user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Verify that the user is correct.
    ## Get each account's follower count.
    a_follower_count = account_a["follower_count"] # Account A follower count
    b_follower_count = account_b["follower_count"] # Account B follower count
    is_correct = check_answer(guess, a_follower_count, b_follower_count) # Compare the 2 accounts and return the letter A or B, depending on which one has more followers

    clear()
    print(logo)

    # Score maintenance.
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}.")