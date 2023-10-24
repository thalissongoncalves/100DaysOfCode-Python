import art
from replit import clear

print(art.logo)
print("Welcome to the secret auction program")

offer_list = []


def blind_auctions():
    name = input("What is your name?: ")
    money = input("What's your bid?: R$ ")
    new_offer = {
        "name": name,
        "bid": money
    }
    offer_list.append(new_offer)
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if question == "yes":
        clear()
        blind_auctions()
    else:
        biggest_value = 0
        for offer in offer_list:
            if biggest_value < int(offer["bid"]):
                biggest_value = int(offer["bid"])
        for name_of_biggest_value in offer_list:
            if int(name_of_biggest_value["bid"]) == biggest_value:
                print(f"The winner is {name_of_biggest_value['name']} with a bid of R$ {int(name_of_biggest_value['bid'])}")
    

blind_auctions()