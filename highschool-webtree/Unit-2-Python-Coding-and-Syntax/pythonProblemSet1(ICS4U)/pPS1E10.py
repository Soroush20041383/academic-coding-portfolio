"""
10. Create a program that allows the user to input their name.
Create variables to save the input as a string and a List of
individual letters. Write code (or functions) that “rotate” the
letters in the object (meaning, if you are given the string “Nick”
or List [N, i, c, k], then rotating the letters left (or CCW) by one
would create “ickN” or [i, c, k, N].
Rotate the Letters left (or CCW) if there are an odd number of
vowels
Rotate the Letters right (or CW) if there are an even number of
vowels
Rotate the letters positions half of the original string’s/list’s
length
Hint, you may want to use the list/tuple/set
vowels = [a, A, e, E, i, I, o, O, u, U]
"""
def rotate_letters_left(name):
    return name[1:] + [name[0]]

def rotate_letters_right(name):
    return [name[-1]] + name[:-1]

# Get user input for their name
user_name = input("Enter your name: ")

# Convert the name to lowercase
lowercase_name = user_name.lower()

# Create a list of individual letters
letters_list = list(lowercase_name)

# Define the set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Determine the number of vowels in the name
num_vowels = sum(letter in vowels for letter in lowercase_name)

# Calculate the rotation amount
rotation_amount = len(letters_list) // 2

# Perform rotation based on the number of vowels
if num_vowels % 2 == 1:
    rotated_name = rotate_letters_left(letters_list)
else:
    rotated_name = rotate_letters_right(letters_list)

# Perform rotation by the calculated rotation amount
rotated_name = rotated_name[rotation_amount:] + rotated_name[:rotation_amount]

# Convert the list back to a string
rotated_name = ''.join(rotated_name)

# Output the result
print("Original Name:", user_name)
print("Rotated Name:", rotated_name)
