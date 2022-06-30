import sys 
from collections import deque 

N, M, V = map(int, input().split(' '))
visited = [0 for _ in range(N+1)]
connected = []
for i in range(N+1):
    connected.append([0 for _ in range(N+1)])
for i in range(M):
    start, end = map(int, input().split(' '))
    connected[start][end] = 1 
    connected[end][start] = 1
def bfs(start):
    result = []
    que = deque()
    que.append(start)
    while que:
        val = que.popleft()
        if visited[val] == 0:
            result.append(val)
            visited[val] = 1
        for i in range(1,N+1):
            if visited[i] == 0 and connected[val][i] == 1:
                que.append(i)
    return result
def dfs(start):
    result =[]
    lst = deque()
    lst.append(start)
    while lst:
        val = lst.pop() # 오른쪽꺼 
        if visited[val] == 0:
            result.append(val)
            visited[val] =1 
        for i in range(N,0,-1): # 거꾸로 넣어줌으로써 stack 형태로 표현 
            if visited[i] == 0 and connected[val][i] == 1:
                lst.append(i)
                
    return result 


print(*dfs(V))
visited = [ 0 for _ in range(N+1)]
print(*bfs(V))

