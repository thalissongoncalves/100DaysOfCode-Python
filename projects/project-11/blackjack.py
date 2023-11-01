from art import logo
import random

print(logo)
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

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
    print(f"Your cards: {two_cards_player}, current score: {sum_player}")
    print(f"Computer's first card: {cards_computer[0]}")
    def return_score(sum_player):
        pass_or_get = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        ask = True
        if pass_or_get == 'y':
            while ask:
                for card in range(0, 1):
                    random_card_one = random.choice(cards)
                    two_cards_player.append(random_card_one)
                    sum_player += random_card_one
                ask = False
                print(f"Your cards: {two_cards_player}, current score: {sum_player}")
                print(f"Computer's first card: {cards_computer[0]}")
                return_score(sum_player)
        if pass_or_get == 'n':
            print(f"Your final hand: {two_cards_player}, final score: {sum_player}")
            print(f"Computer's final hand: {cards_computer}, final score: {sum_computer}")
            if sum_player == 21:
                print(f"You win!")
            elif sum_computer == 21:
                print(f"Computer's win!")
            elif sum_player > 21:
                print(f"Computer's win!")
            elif sum_computer > 21:
                print(f"You win!")
            elif sum_player < sum_computer:
                print(f"Computer's win!")
            elif sum_computer < sum_player:
                print(f"You win!")
            elif sum_player == sum_computer:
                print(f"Draw!")
    return_score(sum_player)

if start_game == 'y':
    blackjack()
else:
    print("Okay, see you later")