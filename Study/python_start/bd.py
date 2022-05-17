import sys 
#sys.setrecursionlimit(10**7)

input = sys.stdin.readline
node , lines , root_node = map(int, input().split(' '))
graph_list = {}
'''
# 테스트용
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}

root_node = 1
'''
'''
# my method 
result_lst = []
result_lst.append(root_node)
visited = [0 for _ in range(len(list(graph_list.keys()))+1)]
visited[root_node] = 1 

def dfs(lst, current, result):
    for i in range(len(list(lst[current]))):
        print(lst[current])
        temp_lst = list(lst[current])
        val = temp_lst[i]
        if visited[val] != 1:
            visited[val] = 1
            result.append(val)
            dfs(lst, val, result)
        
dfs(graph_list, root_node, result_lst)
print(*result_lst)
'''

for i in range(node): # graph_list는 그래프들이며 처음에는 노드 개수만큼 초기화 
    graph_list[i+1] = []

for i in range(lines):
    start , end = map(int, input().split(' '))
    graph_list[start].append(end)
    graph_list[end].append(start)
for i in range(node):
    graph_list[i+1] = sorted(graph_list[i+1])
#print(graph_list)
# use stack no recursion
visited = []
visited_node = [] # stack 구현 
visited_node.append(root_node)
visited.append(root_node)

def dfs(lst):
    
    current = visited_node.pop()
    temp_lst = list(graph_list[current])
    for i in range(len(temp_lst)):
        val = temp_lst[i]
        if val not in visited:
            visited.append(val)
            visited_node.append(val)
            dfs(lst)

dfs(graph_list)

print(*visited)


## bfs queue

visited = []
visited_node = [] # stack 구현 
visited_node.append(root_node)
visited.append(root_node)

def bfs(graph,root):
    while visited_node:
        current = visited_node.pop(0)
        temp_list = list(graph[current])
        for i in range(len(temp_list)):
            val = temp_list[i]
            if val not in visited:
                visited.append(val)
                visited_node.append(val)

bfs(graph_list, root_node)

print(*visited)
