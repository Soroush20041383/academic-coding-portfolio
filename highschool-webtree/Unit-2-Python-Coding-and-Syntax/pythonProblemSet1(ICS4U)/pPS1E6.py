"""
6. Write a program that allows the user to input the sides of a right
angle triangle in the following two styles “4, 5” or “4,5”. Use the
split and strip method to method to separate and save the
values and calculate the hypotenuse
"""
import math

def calculate_hypotenuse(side1, side2):
    hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
    return hypotenuse

# Get user input for the sides of the triangle
user_input = input("Enter the sides of the right-angle triangle (separated by a comma): ")

# Split the input and strip any leading/trailing whitespace
sides = user_input.split(",")
side1 = float(sides[0].strip())
side2 = float(sides[1].strip())

# Calculate the hypotenuse
hypotenuse = calculate_hypotenuse(side1, side2)

# Output the result
print("Hypotenuse:", hypotenuse)
