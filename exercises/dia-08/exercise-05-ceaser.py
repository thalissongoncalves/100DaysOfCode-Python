alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(direction_input, text_input, shift_input):
    word = ""
    for letter in text_input:
        index = alphabet.index(f"{letter}")
        if direction_input == "encode":
            word += alphabet[index + shift_input]
        elif direction_input == "decode":
            word += alphabet[index - shift_input]
    if direction_input == "encode":
        print(f"The encoded text is {word}")
    elif direction_input == "decode":
        print(f"The decoded text is {word}")

ceaser(direction_input=direction, text_input=text, shift_input=shift)