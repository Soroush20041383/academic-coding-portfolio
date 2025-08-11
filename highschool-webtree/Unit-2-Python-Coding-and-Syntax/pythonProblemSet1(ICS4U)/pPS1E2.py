"""
Write a function named “findThem” that has four parameters
(pMin, pMax, pDivisor, and pNotDivisor). All parameters are
assumed to be integers.The function will return a list of all
numbers that are divisible by pDivisor, but not divisible by
pNotDivisor, between the values of pMin to pMax.
"""
def findThem(pMin, pMax, pDivisor, pNotDivisor):
    numbers = []
    for num in range(pMin, pMax + 1):
        if num % pDivisor == 0 and num % pNotDivisor != 0:
            numbers.append(num)
    return numbers
