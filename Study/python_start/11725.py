import sys
from collections import deque 

A = int(sys.stdin.readline())
check = [0] * (A+1)
matrix = {}
for i in range(1,A+1):
    matrix[i] = []
for i in range(A-1):
    lnode, rnode = map(int, input().split())
    
    matrix[lnode].append(rnode)
    matrix[rnode].append(lnode)
visited = [False for _ in range(A+1)] 
parent_lst = [A+2] * (A+1)
parent_lst[1] = 0
def grade_level():
    que = deque()
    que.append(1)
    while que:
        val = que.pop()
        if visited[val] == False:
            for j in range(len(matrix[val])):

                if matrix[val][j] == 1:
                    parent_lst[val] = 1
                elif parent_lst[matrix[val][j]] != A+2:
                    parent_lst[val] = min(parent_lst[val],matrix[val][j])
                que.append(matrix[val][j])
        visited[val] = True 
            
grade_level()

for i in range(2,A+1):
    print(parent_lst[i])