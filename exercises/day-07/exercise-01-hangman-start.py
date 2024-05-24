#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

input_letter = input("Guess a letter: ")
for word in word_list[random.randint(0, len(word_list)) - 1]:
    for letter in word:
        if letter == input_letter:
            print("Right")
        else:
            print("Wrong")