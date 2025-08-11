import random


def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Generate a list of 20 random integers between 0 and 100
randomList = [random.randint(0, 100) for _ in range(20)]

print("Og List")
print(randomList)

sortedList = insertionSort(randomList)

print("Sorted List (Insertion Sort):")
print(sortedList)
