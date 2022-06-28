import sys 

N, M = map(int, input().split())

maps = []
for i in range(N+1):
    maps.append([0 for _ in range(N+1)])
for i in range(M):
    start, end = map(int, input().split())
    maps[start][end] = 1
    maps[end][start] = 1
visited = [0 for _ in range(N+1)]
loc = []
start = 1
visited[start] = 1
loc.append(start)
stack = []
stack.append(start)
def dfs(stack):
    if stack != []:
        val = stack.pop()
        for i in range(1, N+1):
            if val != i:
                if maps[val][i] == 1 and visited[i] == 0:
                    visited[i] =1 
                    stack.append(i)
                    loc.append(i)
                    dfs(stack)
dfs(stack)
print(loc)