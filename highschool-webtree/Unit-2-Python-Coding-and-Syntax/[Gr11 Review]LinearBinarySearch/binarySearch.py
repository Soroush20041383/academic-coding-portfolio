import random

# Set a specific seed for reproducibility
random.seed(42)

# Function to create a list of integer values
def create_list():
    return [random.randint(0, 100) for _ in range(10)]

# Binary search function
def binary_search(sorted_lst, target):
    start = 0
    end = len(sorted_lst) - 1

    while start <= end:
        mid = (start + end) // 2
        if sorted_lst[mid] == target:
            return mid
        elif sorted_lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Create a list of integer values
my_list = create_list()

# Print the created list
print(f"Created list: {my_list}")

# Sort the list before performing binary search
sorted_list = sorted(my_list)
print(f"Sorted list: {sorted_list}")

# Use a target value for searches
target = sorted_list[0]  # use the first element as target

# Perform binary search
print(f"Binary search result for {target}: Index {binary_search(sorted_list, target)}")
