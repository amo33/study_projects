import sys
from collections import deque 
sys.setrecursionlimit(5000) 
N = int(input())


scc_lst = list()
lst =deque()
def scc(start, parent_lst, visited, total_lines):
    parent_lst[start] = start
    parent = start 
 
    lst.append(start)
        
    for i in range(len(parent_lst)):
        if total_lines[start][i] != 0:
            if parent_lst[i] == 0:
                parent = min(parent, scc(i,parent_lst, visited, total_lines))
            elif visited[i] == 0:
                parent = min(parent, parent_lst[i])
    if parent == parent_lst[start]:
        temp = []
        while True:
            val = lst.pop() # stack으로 진행 
            if visited[val] != 1:
                visited[val] =1 
                temp.append(val)
                if val == parent:
                    scc_lst.append(temp)
                    break 
    return parent
for j in range(N):
    scc_lst= []
    total_node = int(input())
    lst = list(map(int, input().split(' ')))
    actual_lst = [i+1 for i in range(total_node)]
    total_lines = []
    for i in range(total_node+1):
        total_lines.append([0 for _ in range(total_node+1)])
    for i in range(len(actual_lst)):
        total_lines[actual_lst[i]][lst[i]] = 1 # 간선 정리 
    parent_lst = [0 for _ in range(total_node+1)]
    visited = [0 for _ in range(total_node+1)]
    for i in range(1, total_node+1):
        if visited[i] == 0:
            scc(i, parent_lst, visited, total_lines)
    print(len(scc_lst))