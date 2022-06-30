import sys 

<<<<<<< HEAD
N = int(input())
M = int(input())
visited = [0 for _ in range(N+1)]
tracked = []
map = []
stack =[]
stack = []
start = 1
stack.append(start)
tracked.append(start)
def dfs(stack):
    while stack != []:
        val = stack.pop()
        for i in range(1,N+1):
            if i != val:
                if map[val][i] == 1 and visited[i]== 0:
                    tracked.append(i)
                    stack.append(i)
for i in range(N+1):
    map = [0 for _ in range(N+1)]
for i in range(M):
    start, end = map(int, input().split())
    map[start][end] = 1
    map[end][start] = 1
dfs(stack)
print(tracked)
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
=======
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
>>>>>>> 0b958d3b53963536b29cf6101796e8a2fe8c9c24
