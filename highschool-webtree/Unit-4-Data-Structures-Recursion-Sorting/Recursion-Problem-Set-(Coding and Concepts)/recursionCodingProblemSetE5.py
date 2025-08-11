def linearSearch(arr, target, index=0):
    # Base case 1: If the array is empty, the target is not in the array
    if len(arr) == 0:
        return -1
    # Base case 2: If the first element of the array is the target, return the index
    elif arr[0] == target:
        return index
    # Recursive case: Call linearSearch on the rest of the array
    else:
        return linearSearch(arr[1:], target, index + 1)

print(linearSearch([1, 2, 3, 4, 5], 4))  # Output: 3
print(linearSearch([1, 2, 3, 4, 5], 6))  # Output: -1
