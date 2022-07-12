import sys 
sys.setrecursionlimit(10**6)
dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,1,-1,-1,1,-1,1]

def dfs(x,y,visited,map_loc):
    for i in range(8):
        x_t = x+ dx[i]
        y_t = y + dy[i]
        # print(visited) 
        # print(x_t, y_t)
        if (0<=x_t and x_t <len(map_loc)) and (0<=y_t and y_t<len(map_loc[0])) :
            if visited[x_t][y_t] == False and map_loc[x_t][y_t] == 1:
                visited[x_t][y_t] = True
                dfs(x_t,y_t,visited,map_loc)
while True:
    
    cnt = 0
    w, h = map(int, sys.stdin.readline().strip().split())
    if w==0 and h==0:
        break
    map_loc = []
    visited = []
    for i in range(h):
        map_loc.append(list(map(int,sys.stdin.readline().strip().split())))
        visited.append([False for _ in range(w)])
    # print(visited)
    for i in range(h):
        for j in range(w):
            if map_loc[i][j] == 1 and visited[i][j] == False:
                cnt +=1 
                visited[i][j] = True
                dfs(i,j,visited,map_loc)
    print(cnt)
    