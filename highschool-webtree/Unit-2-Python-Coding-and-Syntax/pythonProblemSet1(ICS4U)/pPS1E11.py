"""
11. Create a two square 2D Array (both 3x3) First 2D Array
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

[1, 2, 3]

[8, X, 4]
[7, 6, 5]

Are rotate the 2D array about the center object (the “5” or the
“X”). You only have to rotate the 1 set in either direction. You
have permission to look around on the internet, BUT you will run
into the “zip()” function. (one of Python’s built in functions)
"""
# Create the first 2D array
array1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create the second 2D array
array2 = [
    [1, 2, 3],
    [8, 'X', 4],
    [7, 6, 5]
]

# Rotate the second array about its center object
rotated_array2 = list(zip(*reversed(array2)))

# Output the results
print("Original Array 1:")
for row in array1:
    print(row)

print("\nOriginal Array 2:")
for row in array2:
    print(row)

print("\nRotated Array 2:")
for row in rotated_array2:
    print(row)
