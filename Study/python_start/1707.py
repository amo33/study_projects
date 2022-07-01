import sys 
from collections import deque 
T = int(input())


def bfs(val,visited):
    
    que = deque()
    que.append(val)
    visited[val] =1
    while que:
        # print(que, visited)
        node = que.popleft()
        
        for i in range(len(V_lst[node])):
            #print(V_lst[node])
            if visited[V_lst[node][i]] == 0:
                que.append(V_lst[node][i])
                visited[V_lst[node][i]] = 1 if visited[node] != 1 else 2 
def checkbi(visited):
    for i in range(len(V_lst)):
        if len(V_lst[i]) == 0:
            continue
        # print(V_lst[i])
        for j in range(len(V_lst[i])):
            #print(visited[i], visited[V_lst[i][j]])
            if visited[i] == visited[V_lst[i][j]]:
                return False 
    return True


for i in range(T):
    V, E = map(int, input().split(' '))
    visited = [0 for _ in range(V+1)]
    V_lst = [[] for _ in range(V+1)]
    for j in range(E):
        start, end = map(int, input().split(' '))
        V_lst[start].append(end)
        V_lst[end].append(start)
    flg = 1
    for k in range(1,V+1):
            # visited = [0 for _ in range(V+1)]
            if visited[k] == 0 and len(V_lst[k]) != 0:
                bfs(k,visited)  
    # print(visited)         
    if checkbi(visited) == False:
        print("NO")
    else:
        print("YES")