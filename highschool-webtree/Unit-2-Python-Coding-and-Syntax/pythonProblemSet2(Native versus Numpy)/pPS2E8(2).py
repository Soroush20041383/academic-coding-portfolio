"""
8. Row and column sums:
Write a function that takes a 2D array as input and returns two
lists: one containing the sum of each row and the other
containing the sum of each column.
"""

import random
random.seed(1)



def row_col_sums(m):
    row_sums = [sum(row) for row in m]
    col_sums = [sum(col) for col in zip(*m)]
    return row_sums, col_sums


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

row_col_sums_res = row_col_sums(matrix_a)
print("Row and Column Sums (Python): ", row_col_sums_res)