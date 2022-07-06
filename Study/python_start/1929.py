import sys , math 
N,M = map(int,input().split())
lst = [i for i in range(N, M+1)]

for val in lst:
    if val != 1:
        flag = 1
        standard = math.floor(val **0.5) 
        for j in range(2,standard+1):
            if val % j == 0:
                flag = 0
                break 
        if flag == 1:
           print(val)