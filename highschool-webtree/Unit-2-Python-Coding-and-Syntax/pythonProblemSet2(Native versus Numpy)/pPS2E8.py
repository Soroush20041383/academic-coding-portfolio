"""
8. Row and column sums:
Write a function that takes a 2D array as input and returns two
lists: one containing the sum of each row and the other
containing the sum of each column.
"""

import numpy as np
import random
random.seed(1)
np.random.seed(1)

def row_col_sums_np(m):
    row_sums = np.sum(m, axis=1)
    col_sums = np.sum(m, axis=0)
    return row_sums, col_sums


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

row_col_sums_res_np = row_col_sums_np(matrix_a)
print("Row and Column Sums (Numpy): ", row_col_sums_res_np)
