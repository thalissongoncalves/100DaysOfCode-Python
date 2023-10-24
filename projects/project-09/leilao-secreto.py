import art
from replit import clear

print(art.logo)
print("Bem-vindo ao programa de leilão secreto")

offer_list = []


def blind_auctions():
    name = input("Qual é o seu nome?: ")
    money = input("Qual é o seu lance?: R$ ")
    new_offer = {
        "name": name,
        "bid": money
    }
    offer_list.append(new_offer)
    question = input("Existem outros licitantes? Digite 'sim' ou 'não'.\n")
    if question == "sim":
        clear()
        blind_auctions()
    elif question == "nao" or question == "não":
        biggest_value = 0
        for offer in offer_list:
            if biggest_value < int(offer["bid"]):
                biggest_value = int(offer["bid"])
        for name_of_biggest_value in offer_list:
            if int(name_of_biggest_value["bid"]) == biggest_value:
                print(f"O vencedor é {name_of_biggest_value['name']} com um lance de R$ {int(name_of_biggest_value['bid'])}")
    

blind_auctions()