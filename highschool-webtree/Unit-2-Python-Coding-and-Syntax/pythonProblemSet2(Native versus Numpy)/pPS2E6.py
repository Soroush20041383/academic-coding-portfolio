"""
6. Rotate matrix 90 degrees clockwise:
Write a function that takes a square 2D array as input and
returns the matrix rotated 90 degrees clockwise.
"""

import numpy as np
import random
random.seed(1)
np.random.seed(1)

def rotate_matrix_np(m):
    return np.rot90(m, -1)



rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

rotated_matrix_np = rotate_matrix_np(matrix_a)
print("Rotated Matrix (Numpy): ", rotated_matrix_np)
