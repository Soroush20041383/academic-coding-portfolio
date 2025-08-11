def findFactorial(pNum):
    # base case
    if pNum == 0 or pNum == 1:
        return 1
    # recursive case
    else:
        return pNum * findFactorial(pNum - 1)

print(findFactorial(5))  # Output: 120
