"""
8. Building off of question 7, write a program to detect if there is at
least 1 copy of each letter of the alphabet in the entire list of
strings. I HIGHLY recommend using sets and their methods
(most likely union, intersection, and difference).
"""

import random
import string

def generate_random_string(length):
    alphabet = string.ascii_lowercase
    random_string = ''.join(random.choice(alphabet) for _ in range(length))
    return random_string

# Create the list of strings
string_list = [generate_random_string(15) for _ in range(10)]

# Combine all strings into a single string
combined_string = ''.join(string_list)

# Create a set of unique letters in the combined string
unique_letters = set(combined_string)

# Create a set of all lowercase letters in the alphabet
all_letters = set(string.ascii_lowercase)

# Check if all letters are present
if unique_letters == all_letters:
    print("All letters of the alphabet are present in the list of strings.")
else:
    missing_letters = all_letters - unique_letters
    print("The following letters are missing:", missing_letters)
