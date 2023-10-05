print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Seja bem-vindo ao game Ilha do Tesouro")
print("Sua missão é procurar pelo tesouro escondido")

#Write your code below this line 👇

question_one = input("Você está em uma encruzilhada. Para onde você deseja ir? Digite 'esquerda' ou 'direita'.\n").lower()
if question_one == "esquerda":
  question_two = input("Você chega a um lago. Há uma ilha no meio do lago. Digite 'esperar' para esperar por um barco. Digite 'nadar' para nadar até lá.\n").lower()
  if question_two == "esperar":
    question_three = input("Você chega à ilha ileso. Há uma casa com 3 portas. Uma 'vermelha', uma 'amarela' e uma 'azul'. Qual cor você escolhe?\n").lower()
    if question_three == "amarela":
      print("Você ganhou!")
    elif question_three == "azul":
      print("Comido por bestas. Fim de jogo.")
    elif question_three == "vermelha":
      print("Queimado pelo fogo. Fim de jogo.")
    else:
      print("Você escolheu uma porta que não existe. Fim de jogo.")
  else:
    print("Você foi atacado por uma truta zangada. Fim de jogo.")
else:
  print("Você caiu em um buraco. Fim de jogo.")