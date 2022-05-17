import sys 
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

total = int(input())

visited = []
home = []
for i in range(total):
    home.append(list(map(int, input())))

def bfs(graph , x, y):

    queue = deque()
    queue.append((x,y))
    count = 1
    graph[x][y] = 0
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            d_x = dx[i] + x
            d_y = dy[i] + y
            if d_x < 0 or d_x >= len(graph) or d_y <0 or d_y >= len(graph):
                continue 
            if graph[d_x][d_y] == 1:
                graph[d_x][d_y] = 0
                queue.append((d_x, d_y))
                count +=1
    return count 

cnt = []
for i in range(total):
    for j in range(total):
        if home[i][j] == 1:
            cnt.append(bfs(home, i,j))
cnt.sort()
print(len(cnt))
for val in cnt:
    print(val)




