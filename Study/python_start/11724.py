# import sys 
# from collections import deque 
# import time
# sys.setrecursionlimit(5000)
# N, M = map(int, input().split(' '))
# connected = []
# result_cc = []
# for i in range(N+1):
#     connected.append([0 for _ in range(N+1)])
# for i in range(M):
#     start , end = map(int, input().split(' '))
#     connected[start][end] = 1
#     connected[end][start] = 1 
# visited = [0 for _ in range(N+1)]
# parent_node = [0 for _ in range(N+1)]
# id =0
# #for i in range(N+1):
#     #parent_node.append(i) #부모 노드 설정 
# lst = deque()
# def check_parent(start):
#     parent_node[start] = start
#     lst.append(start)
#     print(lst)
#     print(parent_node)
#     parent = parent_node[start]

#     for i in range(1,N+1):
#         if connected[start][i] != 0:
#             print("!!!!!",start,i)
#             if parent_node[i] == 0:
#                 print("parent none",start,i)
#                 parent = min(check_parent(i), parent)
#                 #parent_node[start] = parent 
#                 #parent_node[i] = parent 
#                 #lst.append(i)
#             elif visited[i] != 1:
#                 print("visited",start,i)
#                 parent = min(parent_node[i], parent)
#                 print(parent)
#                 #parent_node[start] = parent

#                 #parent_node[i] = parent
#                 #lst.append(i)
#     temp = []
#     #time.sleep(5)
#     if parent == parent_node[start]: # 만약 같다면
#         print("p",parent) 
#         #print(parent)
#         while lst:
#             val = lst.pop()
#             if visited[val] ==0:
#                 temp.append(val)
#                 #print(temp)
#                 visited[val] = 1
#                 if val == parent:
#                     #print(temp)
#                     result_cc.append(temp)
#                     break 
#     #print(parent)
#     return parent
# for i in range(1,N+1):
#     if visited[i] != 1:
#         check_parent(i)
# print(result_cc)
# print(len(result_cc))
# 위 SCC 방식을 해도 좋지 않다. 단방향이 아니기 때문에
import sys 
from collections import deque 
sys.setrecursionlimit(5000)
N, M = map(int, input().split(' '))
connected = []
result_cc = []
for i in range(N+1):
    connected.append([0 for _ in range(N+1)])
for i in range(M):
    start , end = map(int, input().split(' '))
    connected[start][end] = 1
    connected[end][start] = 1 
visited = [0 for _ in range(N+1)]
parent_node = [0 for _ in range(N+1)]
lst = deque()
def dfs(start):
    lst.append(start)
    temp =[]
    while lst:
        val = lst.pop() # stack으로 꺼낸다.
        if visited[val] != 1:
            temp.append(val)
            visited[val] = 1
        for i in range(N,0,-1):
            if connected[val][i] != 0 and visited[i] != 1:
                lst.append(i)
    result_cc.append(temp)

for i in range(1, N+1):
    if visited[i] != 1:
        dfs(i)
print(result_cc)

