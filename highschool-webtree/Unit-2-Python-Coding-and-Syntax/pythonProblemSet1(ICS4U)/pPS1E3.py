"""
Write two functions that can calculate the factorial of a given
number. In one function use a for loop, and in the other
function, use a recursive method.
"""
# Using for loop
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5

result_iterative = factorial_iterative(number)
print("Factorial (using a for loop):", result_iterative)