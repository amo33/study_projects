import sys 

input = sys.stdin.readline 
memoization = [0 for _ in range(1001)]
val = int(input())

def dp(val):
    if val == 1:
        return 1
    elif val == 2:
        return 3 
    if memoization[val] !=0: return memoization[val]
    else:
        memoization[val] = dp(val-1) + 2 * dp(val-2)
        return memoization[val]
print(dp(val) % 10007)
