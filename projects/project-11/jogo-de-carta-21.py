from art import logo
import random

print(logo)
start_game = input("Você quer jogar uma partida de Blackjack? Digite 'y' ou 'n': ").lower()

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_random = [2, 3]
    two_cards_player = []
    cards_computer = []
    sum_player = 0
    sum_computer = 0
    for two in range(0, 2):
        random_card = random.choice(cards)
        two_cards_player.append(random_card)
    for two in range(0, random.choice(computer_random)):
        random_card = random.choice(cards)
        cards_computer.append(random_card)
    for sum_p in two_cards_player:
        sum_player += sum_p
    for sum_c in cards_computer:
        sum_computer += sum_c
    print(f"Suas cartas: {two_cards_player}, Pontuação: {sum_player}")
    print(f"Primeira carta do Computador: {cards_computer[0]}")
    def return_score(sum_player):
        pass_or_get = input("Digite 'y' para obter outro cartão, digite 'n' para passar: ").lower()
        ask = True
        if pass_or_get == 'y':
            while ask:
                for card in range(0, 1):
                    random_card_one = random.choice(cards)
                    two_cards_player.append(random_card_one)
                    sum_player += random_card_one
                ask = False
                print(f"Suas cartas: {two_cards_player}, Pontuação: {sum_player}")
                print(f"Primeira carta do Computador: {cards_computer[0]}")
                return_score(sum_player)
        if pass_or_get == 'n':
            print(f"Sua mão final: {two_cards_player}, Pontuação Final: {sum_player}")
            print(f"Mão final do Computador: {cards_computer}, Pontuação Final: {sum_computer}")
            if sum_player == 21:
                print("Você Ganhou!")
            elif sum_computer == 21:
                print("Computador Ganhou!")
            elif sum_player > 21:
                print("Computador Ganhou!")
            elif sum_computer > 21:
                print("Você Ganhou!")
            elif sum_player < sum_computer:
                print("Computador Ganhou!")
            elif sum_computer < sum_player:
                print("Você Ganhou!")
            elif sum_player == sum_computer:
                print("Empate!")
    return_score(sum_player)

if start_game == 'y':
    blackjack()
else:
    print("Certo, vejo você em breve.")