import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(direction_input, text_input, shift_input):
    word = ""
    for letter in text_input:
        if letter in alphabet:
            index = alphabet.index(f"{letter}")
            if direction_input == "encode":
                word += alphabet[index + shift_input]
            elif direction_input == "decode":
                word += alphabet[index - shift_input]
        else:
            word += letter
    if direction_input == "encode":
        print(f"The encoded text is {word}")
    elif direction_input == "decode":
        print(f"The decoded text is {word}")

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift = shift % 26

ceaser(direction_input=direction, text_input=text, shift_input=shift)
ask = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
while ask == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(direction_input=direction, text_input=text, shift_input=shift)
    ask_two = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if ask_two == "no":
        ask = "no"
print("Goodbye 👋")