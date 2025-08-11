"""
2. Matrix addition:
Write a function that takes two 2D arrays of the same
dimensions as input and returns a new 2D array that is the
element-wise sum of the input arrays.
"""

import numpy as np
import random
random.seed(1)
np.random.seed(1)

def add_matrices_np(a, b):
    return np.add(a, b)


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

sum_matrix_np = add_matrices_np(matrix_a, matrix_b)
print("Sum Matrix (Numpy): ", sum_matrix_np)
