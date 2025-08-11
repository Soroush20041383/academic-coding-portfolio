"""
2. Matrix addition:
Write a function that takes two 2D arrays of the same
dimensions as input and returns a new 2D array that is the
element-wise sum of the input arrays.
"""

import random
random.seed(1)

def add_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

sum_matrix = add_matrices(matrix_a, matrix_b)
print("Sum Matrix (Python): ", sum_matrix)