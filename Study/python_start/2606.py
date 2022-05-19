from collections import deque
import sys 

total_node = int(input())

total_line = int(input())
graph_list = {}
for i in range(1,total_node+1):
    graph_list[i] = []

for i in range(total_line):
    start , end = map(int, input().split(' '))
    graph_list[start].append(end)
    graph_list[end].append(start)
visited = []
visited.append(1)

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for i in range(len(graph[node])):
            val = graph[node][i]
            if val not in visited:
                visited.append(val)
                queue.append(val)
                

bfs(graph_list,1)

print(len(visited)-1)