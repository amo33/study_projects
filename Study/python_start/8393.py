import sys
sys.setrecursionlimit(100000)
num = int(input())

def sum_recursive(val):
    if val ==0:
        return 0
    else:
        return val + sum_recursive(val-1)
print(sum_recursive(num))