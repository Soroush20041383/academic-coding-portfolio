"""
Write a program that creates a list that has ten
strings, each string is composed of 15 randomly selected
lowercase letters from the english alphabet. There are several
ways to do this; using ascii code; using unicode; but the most
common way is to have a pre-made alphabet string
“abcdefghijklmnopqrstuvwxyz” and randomly select for said
string.
"""
import random
import string

def generate_random_string(length):
    alphabet = string.ascii_lowercase
    random_string = ''.join(random.choice(alphabet) for _ in range(length))
    return random_string

# Create the list of strings
string_list = [generate_random_string(15) for _ in range(10)]

# Output the result
for string in string_list:
    print(string)
