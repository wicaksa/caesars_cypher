""" Combined both encrypt and decrypt functions into one function called caesar() that takes in 3 parameters. 
Depending on the direction input, the function will either encrypt or decrypt a user's message. 
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 
               'o', 'p', 'q', 'r', 's', 't', 'u', 
               'v', 'w', 'x', 'y', 'z', 'a', 'b', 
               'c', 'd', 'e', 'f', 'g', 'h', 'i', 
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 
               'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    string_result = ''
    text_list = list(text) 
    counter = shift 
    print(f"Original message: {string_result.join(text_list)}")

    for i in range(0, len(text_list)):
        new_index = alphabet.index(text_list[i]) 
        counter = shift 

        while counter > 0:
            if direction == 'encode':
                if new_index == len(alphabet) - 1: 
                    new_index = 0 
                    counter -= 1
                else:
                    new_index += 1
                    counter -= 1
            elif direction == 'decode':
                if new_index == 0: 
                    new_index = len(alphabet) - 1 
                    counter -= 1
                else:
                    new_index -= 1
                    counter -= 1
        text_list[i] = alphabet[new_index]
    if direction == 'encode':
        print(f"Encoded message : {string_result.join(text_list)}")
    else:
        print(f"Encrypted message: {string_result.join(text_list)}")
 
# End caesar() 

caesar(text, shift, direction)

# End 
