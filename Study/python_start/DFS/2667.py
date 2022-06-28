from collections import deque 
import sys 
sys.setrecursionlimit(10**6)
#위 문제에서 노드의 개수는 최대 100,000개다.

#따라서 dfs는 최대 100,000번 진행되기 때문에 sys.setrecursionlimit(100000) 또는 sys.setrecursionlimit(10**5)만 해도 충분하다.
N = int(input())
visited = []
lines = []
for i in range(N):
    lines.append(list(map(int, input())))
    visited.append([0 for _ in range(N)])
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
que = deque()
result_lst = []
def dfs(x,y):
    que.append((x,y))
    temp = []
    visited[x][y] = 1
    while que:
        temp.append((x,y))
        x, y = que.pop()
        #visited[x][y] =1 
        for i in range(4):
            d_x = x + dx[i]
            d_y = y + dy[i]
            if (0<=d_x and d_x <N) and (0<=d_y and d_y < N):  
                if visited[d_x][d_y] == 0 and lines[d_x][d_y] == 1:
                    visited[d_x][d_y] = 1
                    que.append((d_x, d_y)) 
    result_lst.append(len(temp))
for i in range(N):
    for j in range(N):
        if visited[i][j] ==0 and lines[i][j] == 1:
            #print(i, j)
            dfs(i,j)
print(len(result_lst))
for i in sorted(result_lst):
    print(i)