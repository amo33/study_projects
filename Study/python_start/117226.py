import sys 

memoization = [0 for _ in range(1001)]
val = int(input())

def dp(target):
    if target == 1:
        return 1 
    elif target == 2:
        return 2

    if memoization[target] != 0: return memoization[target]
    else:
        memoization[target] = dp(target-1) +dp(target-2)
        return memoization[target]
print(dp(val) % 10007)
