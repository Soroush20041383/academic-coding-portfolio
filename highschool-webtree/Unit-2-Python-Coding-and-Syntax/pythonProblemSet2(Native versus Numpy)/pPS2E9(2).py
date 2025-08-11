"""
9. Flipping an image:
Write a function that takes a 2D array representing an image
(meaning make a 2D array where each element in the array is a
list of 3 int values AND where each int value is a randint value
between 0-255 to represent the RBG pixel. Write a function that
will flip the array (either vertically of horizontally) WITHOUT
flipping the colour values.
"""

import random
random.seed(1)

def generate_image(m, n):
    return [[[random.randint(0, 255) for _ in range(3)] for _ in range(n)] for _ in range(m)]

def flip_image(img, axis='h'):
    if axis == 'h':
        return img[::-1]
    else:
        return [row[::-1] for row in img]


rows, columns = 3, 4
matrix_a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_b = [[10,11,12], [13,14,15], [16,17,18]]

image = generate_image(3, 3)
print("Generated Image (Python): ", image)
flipped_image = flip_image(image, 'h')
print("Flipped Image (Python): ", flipped_image)