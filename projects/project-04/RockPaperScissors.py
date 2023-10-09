rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
rockPaperScissor = [rock, paper, scissors]
randomOption = random.randint(0, 2)
choiceOfComputer = rockPaperScissor[randomOption]
choiceOfPeople = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choiceOfPeople == 0 and randomOption == 0:
  print(rock)
  print("Computer chose: ")
  print(choiceOfComputer)
  print("It was a draw.")
if choiceOfPeople == 0 and randomOption == 1:
  print(rock)
  print("Computer chose: ")
  print(choiceOfComputer)
  print("You lose.")
if choiceOfPeople == 0 and randomOption == 2:
  print(rock)
  print("Computer chose: ")
  print(choiceOfComputer)
  print("You win!")
if choiceOfPeople == 1 and randomOption == 0:
  print(paper)
  print("Computer chose: ")
  print(choiceOfComputer)
  print("You win!")
if choiceOfPeople == 1 and randomOption == 1:
  print(paper)
  print("Computer chose: ")
  print(choiceOfComputer)
  print("It was a draw.")
if choiceOfPeople == 1 and randomOption == 2:
  print(paper)
  print("Computer chose: ")
  print(choiceOfComputer)
  print("You lose.")
if choiceOfPeople == 2 and randomOption == 0:
  print(scissors)
  print("Computer chose: ")
  print(choiceOfComputer)
  print("You lose.")
if choiceOfPeople == 2 and randomOption == 1:
  print(scissors)
  print("Computer chose: ")
  print(choiceOfComputer)
  print("You win!")
if choiceOfPeople == 2 and randomOption == 2:
  print(scissors)
  print("Computer chose: ")
  print(choiceOfComputer)
  print("It was a draw.")