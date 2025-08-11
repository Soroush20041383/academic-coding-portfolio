def calculateSum(pList):
    # base case: if the list is empty, return 0
    if len(pList) == 0:
        return 0
    else:
        # recursive case: return the first element of the list plus the sum of the rest of the list
        return pList[0] + calculateSum(pList[1:])

print(calculateSum([1, 2, 3, 4, 5]))  # Output: 15
