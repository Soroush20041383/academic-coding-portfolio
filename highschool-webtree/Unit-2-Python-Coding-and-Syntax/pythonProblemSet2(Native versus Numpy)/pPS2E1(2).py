"""
1. Creating a 2D array:
Write a function that takes two integers, &#39;rows&#39; and &#39;columns&#39;, as
input and returns a 2D array of zeros with the given dimensions.
"""

import random
random.seed(1)


def create_2d_array(rows, columns):
    return [[0 for _ in range(columns)] for _ in range(rows)]


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

created_matrix = create_2d_array(rows, columns)
print("Created Matrix (Python): ", created_matrix)