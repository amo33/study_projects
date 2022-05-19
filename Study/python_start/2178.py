from collections import deque
import sys


height, width = map(int , input().split(' '))

road = []
count = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
max_val = width*height
for i in range(height):
    road.append(list(map(int, input())))
    count.append([max_val for _ in range(width)])
count[0][0] = 1
road[0][0] = 0
def bfs(graph, a,b):
    loc = deque()
    loc.append((a,b))
    while loc:
        x , y = loc.popleft()
        for i in range(4):
            d_x = x+ dx[i]
            d_y = y+ dy[i]
            if d_x < 0 or d_x >= height or d_y <0 or d_y >= width:
                continue
            if graph[d_x][d_y] == 1:
                #print(d_x, d_y)
                graph[d_x][d_y] = 0
                count[d_x][d_y] = min(count[d_x][d_y]+1, count[x][y] + 1)
                if d_x ==height-1 and d_y == width - 1:
                    return count[d_x][d_y]
                loc.append((d_x, d_y))
print(bfs(road, 0,0))
#print(*count)