""" This function decrypt's the user's message. 

User inputs a word and each letter of the word will be shifted according to a given value.
The result is a word that is the decrypted message. 

"""



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    string_result = ''
    text_list = list(text) 
    counter = shift 
    print(f"Original message: {string_result.join(text_list)}")
    for i in range(0, len(text_list)):
        new_index = alphabet.index(text_list[i]) 
        counter = shift 
        while counter > 0:
            if new_index == len(alphabet) - 1: 
                new_index = 0 
                counter -= 1
            else:
                new_index += 1
                counter -= 1
        text_list[i] = alphabet[new_index]
    print(f"Encoded message : {string_result.join(text_list)}")

def decrypt(text, shift):
    string_result = ''
    text_list = list(text) 
    counter = shift 
    print(f"Encrypted message: {string_result.join(text_list)}")
    for i in range(0, len(text_list)):
        new_index = alphabet.index(text_list[i]) 
        counter = shift 
        while counter > 0:
            if new_index == 0: 
                new_index = len(alphabet) - 1 
                counter -= 1
            else:
                new_index -= 1
                counter -= 1
        text_list[i] = alphabet[new_index]
    print(f"Decrypted message : {string_result.join(text_list)}")
# decrypt(text, shift)

def encrypt_or_decrypt(text, shift, direction):
    if direction == 'encode':
        encrypt(text, shift)
    else:
        decrypt(text, shift)

# End 
