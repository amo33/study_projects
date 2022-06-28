import sys 
from collections import deque

INF = 100000
N = int(input())
sys.setrecursionlimit(N)
d = [-1 for _ in range(N+1)]
connected = [[0 for _ in range(N+1)] for _ in range(N+1)]
c = [[0 for _ in range(N+1)] for _ in range(N+1)]
f = [[0 for _ in range(N+1)] for _ in range(N+1)]

def edmond_karp(start, end):
    storage = deque()
    result = 0 
    while True:
        d = [-1 for _ in range(N+1)]
        storage.append(start) # 계속 start 노드에서부터 찾는다. 
        while storage:
            val = storage.popleft() # bfs니까 queue로 푼다. 
            for i in range(len(connected[val])): # 연결된 노드들 중 찾는다. 
                if d[i] ==-1 and connected[val][i] == 1 and c[val][i] - f[val][i] >0:
                    storage.append(i) # 만약 잔여 유량이 있다면 append 
                    d[i] =val # 어느 접점과 연결되어 있는지 확인 
                    if d[end] == val: break # end가 val 이면 하나의 경로를 찾았기에 break하고 이후 작업 진행 
        if d[end] == -1: break # 유량 남는게 없다는 것이므로 끝낸다. -> 이걸로 while True 탈출 
        inf = INF 
        k = d[end] # 마지막 sink에서 연결되었던 노드 값 연결 
        end_index = end # c, f 접근을 위해 필요 
        while True:
            try:
                if k == 1:
                    break 
                inf = min(inf, c[k][end_index] - f[k][end_index]) # 유량 중 제일 작은거를 유량으로 선택 
                end_index = k
                k = d[k]
            except:
                break
        k = d[end]
        end_index = end  
        while True:
            try:
                if k == 1:
                    break
                f[k][end_index] += inf # 유량 추가 
                f[end_index][k] -= inf  # 음의 유량 추가 
                end_index = k
                k = d[k]
            except:
                break 
        result+= inf # 유량 찾은거 추가 
    return result
M = int(input())
for i in range(M):
    start, end, capacity = map(int, input().split(' '))
    connected[start][end] = 1
    connected[end][start] =1 
    c[start][end] = capacity


print(edmond_karp(1, N))
