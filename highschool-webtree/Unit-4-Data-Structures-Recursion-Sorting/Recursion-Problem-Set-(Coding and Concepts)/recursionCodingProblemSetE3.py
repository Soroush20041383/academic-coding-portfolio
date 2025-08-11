def fibonacciNth(n):
    # base case: first and second elements are defined as 0 and 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # recursive case: nth element is the sum of the (n-1)th and (n-2)th elements
        return fibonacciNth(n - 1) + fibonacciNth(n - 2)

def generateFibonacci(pNum):
    return [fibonacciNth(i) for i in range(pNum)]

# Test the functions
print(fibonacciNth(10))  # Output: 55
print(generateFibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
