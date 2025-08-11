"""
4. Transpose of a matrix:
Write a function that takes a 2D array as input and returns its
transpose.
"""

import random
random.seed(1)

def transpose_matrix(m):
    return [list(i) for i in zip(*m)]


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

transposed_matrix = transpose_matrix(matrix_a)
print("Transposed Matrix (Python): ", transposed_matrix)