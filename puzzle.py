import re
import random

puzzle = "I am going to play this game"

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
original_alphabet = list.copy(alphabet)
random.shuffle(alphabet)

key = {original_alphabet[i]: alphabet[i]
       for i in range(len(original_alphabet))}

hashed_puzzle = ""

for letter in puzzle:
    if letter.isspace():
        hashed_puzzle += letter
    else:
        hashed_puzzle += key[letter.upper()]

transformed_puzzle = "   ".join(puzzle.split())
transformed_puzzle = re.sub("[a-zA-Z]", "_", transformed_puzzle)

hashed_puzzle = "   ".join(hashed_puzzle.split())

print(transformed_puzzle)
print(hashed_puzzle)
