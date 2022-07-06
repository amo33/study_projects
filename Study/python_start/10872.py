def factorial(val):
    if val == 0:
        return 1
    return factorial(val-1) * val 
print(factorial(int(input())))