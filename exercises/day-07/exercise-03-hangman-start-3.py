import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in range(word_length):
    display += "_"

success = False
def findLetter():    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

while not success:
    guess = input("Guess a letter: ").lower()
    findLetter()
    for info in display:
        if info != '_':
            success = True
        else:
            success = False

print("You Win!!")