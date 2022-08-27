#Task_1 -> Write an ASCII table in the form of a dictionary
import json

generated_dict = {element : chr(element) for element in range(128)}

print(f'ASCII table in the form of a dictionary: \n {json.dumps(generated_dict, indent=1)}')

# # json hasn't been taught yet, but I wanted to display dictionary values nicely in a column rather than a list.
# # Found a solution on the internet

#Task_2 -> Caesar cipher
print('Caesar cipher')

user_text = input('Please enter any text -> ')
user_number = int(input('Please, enter any integer -> '))

upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z'
                  ]
lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z'
                  ]
ciphertext = []

for letter in user_text:
    if letter in upper_alphabet:
        index = upper_alphabet.index(letter)
        new_index = (index + user_number) % 26
        new_letter = upper_alphabet[new_index]
        ciphertext.append(new_letter)
    elif letter in lower_alphabet:
        index = lower_alphabet.index(letter)
        new_index = (index + user_number) % 26
        new_letter = lower_alphabet[new_index]
        ciphertext.append(new_letter)

print(f"Ciphertext -> {''.join(ciphertext) }")

#Task_2 -> Caesar decoder
print('Caesar decoder')

user_text_1 = input('Please enter any text -> ')
user_number_1 = int(input('Please, enter any integer -> '))

upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z'
                  ]
lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z'
                  ]
deciphered_text = []

for letter_1 in user_text_1:
    if letter_1 in upper_alphabet:
        index_1 = upper_alphabet.index(letter_1)
        new_index_1= (index_1 - user_number_1) % 26
        new_letter_1 = upper_alphabet[new_index_1]
        deciphered_text.append(new_letter_1)
    elif letter_1 in lower_alphabet:
        index_1 = lower_alphabet.index(letter_1)
        new_index_1 = (index_1 - user_number_1) % 26
        new_letter_1 = lower_alphabet[new_index_1]
        deciphered_text.append(new_letter_1)

print(f"Deciphered text -> {''.join(deciphered_text) }")