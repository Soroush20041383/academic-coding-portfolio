"""
4. Write a function that creates a dictionary where the key terms
are 1000 to 1999, and the value is the number of zeroes in the
key term.
{1000:3, ……., 1999:0}
"""
def create_zeroes_dictionary():
    zeroes_dict = {}
    for key in range(1000, 2000):
        count = str(key).count('0')
        zeroes_dict[key] = count
    return zeroes_dict


result = create_zeroes_dictionary()
print(result)
