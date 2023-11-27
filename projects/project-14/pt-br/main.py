from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
    """Pega os dados da conta e retorna o formato imprimível."""
    account_name = account["name"] # Busca o nome no dict
    account_descr = account["description"] # Busca a descrição no dict
    account_country = account["country"] # Busca o país no dict
    return f"{account_name}, um(a) {account_descr}, de {account_country}" # Retorna o nome, descrição e o país juntos

def check_answer(guess, a_followers, b_followers):
    """Pega o palpite do usuário e conta os seguidores e retorna se eles acertarem."""
    if a_followers > b_followers: # Compara o número de seguidores
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True

# Gerando uma conta aleatória de game_data
account_b = random.choice(data)

# Torne o jogo repetível
while game_should_continue:
    # Fazendo com que a conta na posição B se torne a próxima conta na posição A
    account_a = account_b
    account_b = random.choice(data)

    # Para evitar perguntas comparações iguais
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Contra B: {format_data(account_b)}.")

    # Peça um palpite ao usuário.
    guess = input("Quem tem mais followers? Digite 'A' ou 'B': ").lower()

    # Verifique se o usuário está correto.
    ## Obtenha a contagem de seguidores de cada conta.
    a_follower_count = account_a["follower_count"] # Contagem de seguidor da conta A
    b_follower_count = account_b["follower_count"] # Contagem de seguidor da conta B
    is_correct = check_answer(guess, a_follower_count, b_follower_count) # Compare as 2 contas e retorna a letra A ou B, depende de qual tem mais seguidor

    clear()
    print(logo)

    # Manutenção de pontuação.
    if is_correct:
      score += 1
      print(f"Você tem razão! Pontuação atual: {score}.")
    else:
      game_should_continue = False
      print(f"Desculpe, isso está errado. Pontuação final: {score}.")