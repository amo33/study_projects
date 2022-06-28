import sys 
from collections import deque

n = 6
result = 0
INF= 1000000
result = 0 
c = []
f = []
d = [-1 for _ in range(10)] # 방문했는지 확인 
a = [] # 연결된 간선 확인 
for i in range(10):
    c.append([0 for _ in range(10)]) # 총 용랼 
    f.append([0 for _ in range(10)]) # 현재 보내지는 용량 
    a.append([0 for _ in range(10)])
def maxFlow(start,end):
    global result
    while True:
        for i in range(10):
            d[i] = -1
        lst = deque()
        lst.append(start)
        while lst:
            val = lst.popleft()
            print(val)
            for i in range(10):
                y = a[val][i]
                #방문 안했고 용량이 남은 경우 
                if d[y] == -1 and c[val][y] - f[val][y] > 0: # 아예 아직 visit X 
                    lst.append(y)
                    d[y] = val # 경로 기억하기 위해서 이렇게 저장
                    if y == end: break 
        if(d[end] == -1): break # while true 탈출 
        flow = INF
        indx = d[end] 
        while True:
            try:
                flow = min(flow, c[d[indx]][indx] - f[d[indx]][indx])
                indx = d[indx]
                if indx == start:
                    break 
            except:
                break 

        i = d[end] 
        while True:
            try:
                f[d[i]][i] += flow 
                f[i][d[i]] -= flow 
                i = d[i]
                if i == start:
                    break
            except:
                break 

        result += flow
a[1][2] = 2
a[2][1] = 1
c[1][2] = 12 

a[1][4] = 4
a[4][1] = 1
c[1][4] = 11

a[2][3] = 3
a[3][2] = 2 
c[2][3] = 6

a[2][4] = 4
a[4][2] = 2
c[2][4] = 3

a[2][5] = 5 
a[5][2] = 2
c[2][5] = 5

a[2][6] = 6
a[6][2] = 2
c[2][6] = 9

a[3][6] = 6
a[6][3] = 3 
c[3][6] = 8

a[4][5] = 5
a[5][4] = 4
c[4][5] = 9

a[5][3] = 3
a[3][5] =5 
c[5][3] =3 

a[5][6] = 6
a[6][5] = 5
c[5][6] = 4 

maxFlow(1, 6)
print(result)
print(*c)
print(*f)