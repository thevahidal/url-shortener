
from string import ascii_letters, digits
from random import randint

ALPHABET = ascii_letters + digits
def generate_random_string(length = 10):
    string = ""
    
    for i in range(length):
        string += ALPHABET[randint(0, len(ALPHABET) - 1)]

    return string 