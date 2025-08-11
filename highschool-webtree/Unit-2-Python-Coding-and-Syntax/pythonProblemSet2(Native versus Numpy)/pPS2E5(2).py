"""
5. Diagonal elements:
Write a function that takes a square 2D array as input and
returns a list containing its diagonal elements.
"""

import random
random.seed(1)

def get_diagonal(m):
    return [m[i][i] for i in range(len(m))]


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

diagonal_elements = get_diagonal(matrix_a)
print("Diagonal Elements (Python): ", diagonal_elements)