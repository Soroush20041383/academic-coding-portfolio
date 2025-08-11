import random

# Set a specific seed for reproducibility
random.seed(42)

# Function to create a list of integer values
def create_list():
    return [random.randint(0, 100) for _ in range(10)]

# Linear search function
def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1

# Create a list of integer values
my_list = create_list()

# Print the created list
print(f"Created list: {my_list}")

# Use a target value for searches
target = my_list[0]  # use the first element as target

# Perform linear search
print(f"Linear search result for {target}: Index {linear_search(my_list, target)}")