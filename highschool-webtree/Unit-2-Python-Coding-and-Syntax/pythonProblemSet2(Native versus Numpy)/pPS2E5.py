"""
5. Diagonal elements:
Write a function that takes a square 2D array as input and
returns a list containing its diagonal elements.
"""

import numpy as np
import random
random.seed(1)
np.random.seed(1)

def get_diagonal_np(m):
    return np.diagonal(m)


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

diagonal_elements_np = get_diagonal_np(matrix_a)
print("Diagonal Elements (Numpy): ", diagonal_elements_np)