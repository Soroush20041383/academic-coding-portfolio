"""
7. Maximum value and its position:
Write a function that takes a 2D array as input and returns the
maximum value and its position (row, column) in the array.
"""

import numpy as np
import random
random.seed(1)
np.random.seed(1)

def max_value_position_np(m):
    max_val = np.max(m)
    position = np.where(m == max_val)
    return max_val, list(zip(*position))


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

max_val_pos_np = max_value_position_np(matrix_a)
print("Max Value and Position (Numpy): ", max_val_pos_np)
