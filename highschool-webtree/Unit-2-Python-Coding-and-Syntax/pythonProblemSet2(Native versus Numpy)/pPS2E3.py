"""
3. Matrix multiplication:
Write a function that takes two 2D arrays, A and B, as input and
returns their matrix product, AB, if the dimensions are valid for
matrix multiplication. If the dimensions are not valid, return an
error message.
"""

import numpy as np
import random
random.seed(1)
np.random.seed(1)

def multiply_matrices_np(a, b):
    try:
        return np.dot(a, b)
    except ValueError:
        return "Invalid dimensions for matrix multiplication"


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

product_matrix_np = multiply_matrices_np(matrix_a, matrix_b)
print("Product Matrix (Numpy): ", product_matrix_np)