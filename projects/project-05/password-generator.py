#Password Generator Project
import random
from random import sample
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

passwordEazy = ""

for letter in range(0, nr_letters):
  random_letters = random.randint(0, len(letters) - 1)
  passwordEazy += letters[random_letters]

for symbol in range(0, nr_symbols):
  random_symbols = random.randint(0, len(symbols) - 1)
  passwordEazy += symbols[random_symbols]

for number in range(0, nr_numbers):
  random_numbers = random.randint(0, len(numbers) - 1)
  passwordEazy += numbers[random_numbers]

print(f"Here is your password: {passwordEazy}")
  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwordHard = ""

for letter in range(0, nr_letters):
  random_letters = random.randint(0, len(letters) - 1)
  passwordHard += letters[random_letters]
  
for symbol in range(0, nr_symbols):
  random_symbols = random.randint(0, len(symbols) - 1)
  passwordHard += symbols[random_symbols]
  
for number in range(0, nr_numbers):
  random_numbers = random.randint(0, len(numbers) - 1)
  passwordHard += numbers[random_numbers]

samplePassword = sample(passwordHard, len(passwordHard))
samplePasswordStr = ''.join(samplePassword)

print(f"Here is your password: {samplePasswordStr}")