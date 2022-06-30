import sys 

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