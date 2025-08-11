def listSum(pList):
    if len(pList) == 0:
        return 0
    else:
        return pList[0] + listSum(pList[1:])
print(listSum([1, 2, 3, 4, 5]))