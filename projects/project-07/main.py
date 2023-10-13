import random
import hangman_words
import hangman_art

#Defines the list of words in the variable, chooses a random one from the list, and counts how many characters this word has
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Print the game logo
print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

lettersUsed = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Prints a message saying that the user has already used a letter that has already been attempted
    for used in lettersUsed:
        if guess == used:
            print(f"You've already guessed: {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            lettersUsed += guess

    #Check if user is wrong.
    if guess not in chosen_word:
        #Prints the message saying that one life was reduced by your mistake and if the life is equal to 0, the user loses
        print(f"You guessed: {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Print stage of little man being hanged
    print(hangman_art.stages[lives])