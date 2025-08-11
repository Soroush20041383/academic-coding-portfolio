"""
7. Maximum value and its position:
Write a function that takes a 2D array as input and returns the
maximum value and its position (row, column) in the array.
"""

import random
random.seed(1)

def max_value_position(m):
    max_val = max(map(max, m))
    position = [(i, j) for i in range(len(m)) for j in range(len(m[i])) if m[i][j] == max_val]
    return max_val, position


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

max_val_pos = max_value_position(matrix_a)
print("Max Value and Position (Python): ", max_val_pos)