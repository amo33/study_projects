import sys 
import math 
input = sys.stdin.readline
memoization = [0 for _ in range(31)]
val = int(input())
def dp(val):
    if val ==0:
        return 1
    if val == 1:
        return 0
    elif val == 2:
        return 3 
    if memoization[val] !=0: return memoization[val]
    else:
        memoization[val]+= 3*dp(val-2)
        idx = 3
        while idx <=val:
            if idx % 2 ==0:
                memoization[val]+= 2*dp(val - idx)
            idx +=1
        return memoization[val]
print(dp(val))
