import random


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    # Recursive calls for sorting the two halves
    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    # Merge the sorted halves
    sortedArr = merge(leftHalf, rightHalf)
    return sortedArr


def merge(left, right):
    merged = []
    i = j = 0

    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Generate a list of 20 random integers between 0 and 100
randomList = [random.randint(0, 100) for _ in range(20)]

print("Original List:")
print(randomList)

sortedList = mergeSort(randomList)

print("Sorted List (Merge Sort):")
print(sortedList)
