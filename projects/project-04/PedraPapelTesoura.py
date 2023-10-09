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
choiceOfPeople = int(input("Qual você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
if choiceOfPeople == 0 and randomOption == 0:
  print(rock)
  print("Vez do computador: ")
  print(choiceOfComputer)
  print("Deu empate!")
if choiceOfPeople == 0 and randomOption == 1:
  print(rock)
  print("Vez do computador: ")
  print(choiceOfComputer)
  print("Você perdeu.")
if choiceOfPeople == 0 and randomOption == 2:
  print(rock)
  print("Vez do computador: ")
  print(choiceOfComputer)
  print("Você ganhou!")
if choiceOfPeople == 1 and randomOption == 0:
  print(paper)
  print("Vez do computador: ")
  print(choiceOfComputer)
  print("Você ganhou!")
if choiceOfPeople == 1 and randomOption == 1:
  print(paper)
  print("Vez do computador: ")
  print(choiceOfComputer)
  print("Deu empate!")
if choiceOfPeople == 1 and randomOption == 2:
  print(paper)
  print("Vez do computador: ")
  print(choiceOfComputer)
  print("Você perdeu.")
if choiceOfPeople == 2 and randomOption == 0:
  print(scissors)
  print("Vez do computador: ")
  print(choiceOfComputer)
  print("Você perdeu.")
if choiceOfPeople == 2 and randomOption == 1:
  print(scissors)
  print("Vez do computador: ")
  print(choiceOfComputer)
  print("Você ganhou!")
if choiceOfPeople == 2 and randomOption == 2:
  print(scissors)
  print("Vez do computador: ")
  print(choiceOfComputer)
  print("Deu empate!")