import random


def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        minIdx = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIdx]:
                minIdx = j

        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr


# Generate a list of 20 random integers between 0 and 100
randomList = [random.randint(0, 100) for _ in range(20)]

print("Og List:")
print(randomList)

sortedList = selectionSort(randomList)

print("Sorted List (Selection Sort):")
print(sortedList)
