from random import randint
from logo import logo_two
print(logo_two)
print("Bem-vindo ao jogo de adivinhação de números!")
print("Pense em um número entre 1 e 100.")
nivel_difficulty = input("Escolha a dificuldade. Digite 'easy' ou 'hard': ")
number_exactly = randint(0, 100)

def number_guessing(endeavor):
    if endeavor > 0:
        print(f"Você tem {endeavor} tentativas para acertar o número exato.")
        number = int(input("Tente um número: "))
        if number == number_exactly:
            return "Você ganhou"
        elif int(number) > number_exactly:
            print("Muito alto")
        else:
            print("Muito baixo")

        endeavor -= 1
        result = number_guessing(endeavor)

        if result == "Você ganhou":
            return "Você ganhou"
    else:
        print(f"Você ficou sem tentativas, você perdeu. O número correto era {number_exactly}.")

if nivel_difficulty == "hard":
    result = number_guessing(5)
    if result == "Você ganhou":
        print(f"Você acertou! A resposta foi {number_exactly}")
elif nivel_difficulty == "easy":
    result = number_guessing(10)
    if result == "Você ganhou":
        print(f"Você acertou! A resposta foi {number_exactly}")