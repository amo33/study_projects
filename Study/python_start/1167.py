import sys 
from collections import deque 
N = int(input())
tree = {}
for i in range(N+1):
    tree[i] = []
dist = [0] * (N+1)
visited = [False for i in range(N+1)]
for j in range(N):
    input_lst = list(map(int, sys.stdin.readline().strip().split()))
    k =1
    while True:
        if k == len(input_lst)-1:
            break
        # print(k)
        tree[input_lst[0]].append([input_lst[k],input_lst[k+1]]) # 정보 저장 
        k+=2 
        
    
def find_diameter():
    queue = deque()
    queue.append(1)
    while queue:
        val = queue.popleft()
        for i in range(len(tree[val])):
            
            target, distance = tree[val][i]
            if visited[target] == False:
                visited[target] = True
                dist[target] = max(dist[target], dist[val]) + distance
                # print(dist)
                # print(queue)
                queue.append(target)
find_diameter()
print(max(dist)) 
             