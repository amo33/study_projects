import sys
from collections import deque 
N = int(input())

for i in range(N):
    VPS = deque()
    flag = 0
    lst = str(input())
    for j in lst:
        try:
            if j == '(':
                VPS.append(j)
            elif j ==')':
                VPS.pop()
        except:
            print('NO')
            flag = 1
            break
    if flag == 0:
        if len(VPS) != 0:
            print('NO')
        else:
            print('YES')