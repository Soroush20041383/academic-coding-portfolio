def binarySearch(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    # Base case: low and high cross each other, the target is not in the array
    if high < low:
        return -1

    mid = (low + high) // 2

    # Base case: the middle element is the target
    if arr[mid] == target:
        return mid
    # Recursive case 1: the target is less than the middle element
    elif arr[mid] > target:
        return binarySearch(arr, target, low, mid - 1)
    # Recursive case 2: the target is greater than the middle element
    else:
        return binarySearch(arr, target, mid + 1, high)
