def power_recursive(x, n):
    if n == 0:
        if x == 0:
            return "girlie this is undefined"
        else:
            return 1
    else:
        return power_recursive(x, n-1)

print(power_recursive(10, 1))




