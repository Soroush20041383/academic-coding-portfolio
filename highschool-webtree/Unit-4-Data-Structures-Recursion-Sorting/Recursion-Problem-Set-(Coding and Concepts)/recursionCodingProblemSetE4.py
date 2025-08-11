def power(x, n):
    # Base case: x to the power of 0 is 1
    if n == 0:
        return 1
    # Recursive case: x to the power of n is x times x to the power of (n - 1)
    else:
        return x * power(x, n - 1)

print(power(2, 3))  # Output: 8
