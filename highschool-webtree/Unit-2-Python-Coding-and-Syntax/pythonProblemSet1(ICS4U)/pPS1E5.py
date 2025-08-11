"""
5. Write a program that creates a list of 1000 numbers randomly
generated to have values between 5000 and 5100. Then return
the value of the max number in the list and subtract the min
number in the list.
"""
import random

def generate_numbers():
    numbers = []
    for _ in range(1000):
        number = random.randint(5000, 5100)
        numbers.append(number)
    return numbers

def calculate_difference(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    difference = max_num - min_num
    return difference

# Generate the list of numbers
number_list = generate_numbers()

# Calculate the difference between the maximum and minimum numbers
result = calculate_difference(number_list)

# Output the result
print("Maximum number:", max(number_list))
