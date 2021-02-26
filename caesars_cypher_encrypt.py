"""This encrypt function allows users to encrypt a message.

Given a message, the letters of each message will be shifted by a particular value.
The result will be an encrypted message.

"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    string_result = ''
    # Shift each letter of the 'text' forwards in the alphabet by the shift amount. 
    text_list = list(text) # Create a list of the text input by user.
    counter = shift # Keeps track of the number of times to shift the letter.
    print(f"Original message: {string_result.join(text_list)}")

    # Iterate through each element of the list and shift each letter by shift amount.
    for i in range(0, len(text_list)):
        # See what index the current letter is in the alphabet list. 
        new_index = alphabet.index(text_list[i]) 
        counter = shift # Reset counter after each while loop.
        while counter > 0:
            if new_index == len(alphabet) - 1: # If you're at the last index, continue at 
                new_index = 0 # Start at beginning
                counter -= 1
            else:
                new_index += 1
                counter -= 1
        # Replace the current letter in text_list with a new shifted letter
        text_list[i] = alphabet[new_index]
        # print(f"Encrypted message: {text_list}")
    print(f"Encoded message : {string_result.join(text_list)}")

# End 
