"""
Write a program that can find the numbers between 10 and 80
(inclusive) that are divisible by 7 but not divisible by 5.
[14, 21, 28, 42, 49, 56, 63, 77]
"""
def find_numbers():
    numbers = []
    for num in range(10, 81):
        if num % 7 == 0 and num % 5 != 0:
            numbers.append(num)
    return numbers

result = find_numbers()
print(result)
