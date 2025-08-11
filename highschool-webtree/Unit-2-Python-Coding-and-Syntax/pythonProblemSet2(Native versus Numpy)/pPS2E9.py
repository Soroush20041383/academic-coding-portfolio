"""
9. Flipping an image:
Write a function that takes a 2D array representing an image
(meaning make a 2D array where each element in the array is a
list of 3 int values AND where each int value is a randint value
between 0-255 to represent the RBG pixel. Write a function that
will flip the array (either vertically of horizontally) WITHOUT
flipping the colour values.
"""

import numpy as np
import random
random.seed(1)
np.random.seed(1)

def generate_image_np(m, n):
    return np.random.randint(0, 256, (m, n, 3))

def flip_image_np(img, axis='h'):
    if axis == 'h':
        return np.flip(img, 0)
    else:
        return np.flip(img, 1)


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

image_np = generate_image_np(3, 3)
print("Generated Image (Numpy): ", image_np)
flipped_image_np = flip_image_np(image_np, 'h')
print("Flipped Image (Numpy): ", flipped_image_np)