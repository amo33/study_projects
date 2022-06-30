import sys 
import math 
input = sys.stdin.readline
memoization = [0 for _ in range(31)]
val = int(input())
def dp(val):
    if val ==0:
        return 1
    if val % 2 !=0:
        return 0
    elif val == 2:
        memoization[val] = 3
        return 3 
    elif val == 4:
        # idx = int(val/2)
        idx = val
        memoization[idx] = 2 
        return 2 
    if memoization[val] != 0: return memoization[val]
    else: 
        i_d = int(val / 2) 
        #i_d = val
        id = 2 
        #print(i_d)
        while (id <i_d):     
            #print(dp(id))
            if id*2 == val - id*2:
                memoization[val] += dp(id*2) * dp(val-id*2)
            else:
                memoization[val] += 2 * dp(id*2) * dp(val-id*2)
            id += 1 
            if id > i_d:
                break
        return memoization[val]

num = int(val/2)
if val % 2 == 0:
    if val == 0:
        print(0)
    elif val == 2:
        print(3)
    else:
        print(dp(val) + int(pow(3.0, float(num))))
else:
    print(0)