# Realise that the message has been encoded and can be decoded by switching each letter with a corresponding letter.
# Also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.
# For example: "a" is encoded with "z", "b" with "y", "c" with "x", etc

def decode(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ""
    for letter in message:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            decoded_letter_index = (26 - (letter_index + 1)) % 26
            decoded_message += alphabet[decoded_letter_index]
        else:
            decoded_message += letter
    print(decoded_message)

decode("r slkv mlylwb wvxlwvh gsrh nvhhztv")