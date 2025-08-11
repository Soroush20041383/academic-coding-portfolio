import random


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Generate a list of 20 random integers between 0 and 100
randomList = [random.randint(0, 100) for _ in range(20)]

print("Og List:")
print(randomList)

sortedList = bubbleSort(randomList)

print("Sorted List (Bubble Sort):")
print(sortedList)
