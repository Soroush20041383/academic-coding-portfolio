"""
3. Write two functions that can calculate the factorial of a given
number. In one function use a for loop, and in the other
function, use a recursive method.
"""
# Using Recursion
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


number = 5
result_recursive = factorial_recursive(number)
print("Factorial (using recursion):", result_recursive)