import sys 
from collections import deque

val = int(input())
dx =[ 1, -1, 0, 0]
dy = [0, 0, -1, 1]
map_loc = []
visited = [[False]*val for _ in range(val)]
for i in range(val):
    map_loc.append(list(map(int, sys.stdin.readline().rstrip().split())))
    # visited.append(map_loc[i])

queue = deque()

flag = 1

for x in range(val):
    for y in range(val):
        if map_loc[x][y] == 1 and visited[x][y] == False:
            visited[x][y] =True
            queue.append((x,y))
            flag +=1 # scc 형태로 표현 
            # visited[flag] = 0
            while queue:
                loc_x , loc_y = queue.popleft()
               
                end_x, end_y = loc_x, loc_y
                map_loc[loc_x][loc_y] = flag 
                for i in range(4):
                    x_t = loc_x + dx[i]
                    y_t = loc_y + dy[i]
                    if 0<= x_t < val and 0<=y_t < val and map_loc[x_t][y_t]==1 and visited[x_t][y_t] ==False :
                        visited[x_t][y_t] =True # 이거 true false로 잘 해놓자.. 그리고 visited를 해주는 곳을 여기로 잡자 26번째 줄 쪽으로 하면 메모리초과 났다.
                        queue.append((x_t, y_t))
            # print(end_x, end_y)
# for i in range(val):
#     for j in range(val):
#         print(map_loc[i][j],end=' ')
#     print()
# print()
min_val = val*2
def bfs(status_island,min_val,map_info,val):
    # print("{}".format(status_island))
    # map_l = copy.deepcopy(map_info)
    # check = set()
    map_l = map_info
    # print(map_loc)
    dist= [[-1 for _ in range(val)] for _ in range(val)]
    queue = deque()
    for x in range(val):
        for y in range(val):
            if map_l[x][y] == status_island :
                dist[x][y] = 0
                queue.append([x,y])

    while queue:
        loc_x , loc_y= queue.popleft()
       
        # print(loc_x, loc_y,dist, flag)
        for i in range(4):
            x_t = loc_x + dx[i]
            y_t = loc_y + dy[i]
            if 0<= x_t and x_t < val and 0<=y_t and y_t < val:
                # print(visited[x_t][y_t])
                # if visited[x_t][y_t] ==0 and  map_l[x_t][y_t] == 0:
                if map_l[x_t][y_t] == 0 and dist[x_t][y_t]== -1:
                    # print("appended",x_t, y_t, dist+1, flag)
                    # check.add((x_t, y_t))
                    dist[x_t][y_t] = dist[loc_x][loc_y] + 1
                    queue.append([x_t, y_t])
                    
                elif map_l[x_t][y_t] != status_island and map_l[x_t][y_t] > 0:
                    dist[x_t][y_t] = dist[loc_x][loc_y] + 1
                    # dist[x_t][y_t] =1
                    min_val = min(min_val, dist[loc_x][loc_y])
                    return min_val
                                                            
    return min_val
# print("F",flag)
for i in range(2,flag+1):
    # print("i",i)
    return_val = bfs(i, min_val,map_loc, val)
    min_val = min(min_val, return_val)
print(min_val)
# print(min_val)