"""
3. Matrix multiplication:
Write a function that takes two 2D arrays, A and B, as input and
returns their matrix product, AB, if the dimensions are valid for
matrix multiplication. If the dimensions are not valid, return an
error message.
"""

import random
random.seed(1)

def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        return "Invalid dimensions for matrix multiplication"
    return [[sum(x*y for x, y in zip(a_row,b_col)) for b_col in zip(*b)] for a_row in a]


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

product_matrix = multiply_matrices(matrix_a, matrix_b)
print("Product Matrix (Python): ", product_matrix)