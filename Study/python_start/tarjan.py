import sys 
from collections import deque
sys.setrecursionlimit(100000)
id = 0
visited = [ 0 for _ in range(7)]
parent_id = [ -1 for _ in range(7)]
graph_line = []
result_val = []
stored_stack = deque()
print(10)
def dfs2(x):
    global id
    id+=1
    parent_id[x] = id
    parent = id  
    stored_stack.append(x)

    for i in range(len(graph_line[x])):
        if graph_line[x][i] == 1:
            if parent_id[i] == -1:
                parent = min(parent, dfs2(i))
            elif visited[i] != 1: # 이 과정이 왜 필요한걸까?
                parent = min(parent, parent_id[i]) 
    temp_lst = []

    if parent == parent_id[x]:

        while stored_stack:
            print(stored_stack)
            val = stored_stack.pop()
            visited[val] = 1
            temp_lst.append(val+1)
            if val == parent_id[x] - 1:
                break
        result_val.append(temp_lst)
    return parent
graph_line.append([0,1,0,0,0,0,0])
graph_line.append([0,0,1,0,0,0,0])
graph_line.append([1,0,0,0,0,0,0])
graph_line.append([0,0,0,0,1,0,0])
graph_line.append([0,0,0,0,0,0,1])
graph_line.append([0,0,0,0,1,0,0])
graph_line.append([0,0,0,0,0,1,0])
print(20)
for i in range(7):
    if parent_id[i] == -1:
        dfs2(i)
print(parent_id)
print(result_val)