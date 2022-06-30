# max = 101
# vector = [[] for i in range(max + 1)]
# dept = [ 0 for i in range(max + 1)]
# n = 3
# m = 0

# def dfs(x, visited):
#     for v in vector[x]: # 연결된 노트북 것을 순회 
#         t = v
#         if visited[t]: continue #만약 이미 갔다 왔다면 continue
#         visited[t] = True
#         if dept[t] == 0 or dfs(dept[t], visited):
#             dept[t] = x
#             return True
#     return False
    
# def main():
#     vector[1].append(1)
#     vector[1].append(2)
#     vector[1].append(3)
#     vector[2].append(1)
#     vector[3].append(2)
#     count = 0
#     # visited = [ False for i in range(max + 1)]
#     for i in range(1, n + 1):
#         visited = [ False for _ in range(max + 1)] # 새로 체크
#         if dfs(i, visited): count += 1
#     print(f'{count}개의 매칭이 이뤄졌습니다.')
#     for i in range(1, max + 1):
#         if not dept[i] == 0:
#             print(f'{dept[i]} -> {i}')
            
# main()

import sys
N = int(input()) 
sys.setrecursionlimit(N*N)
M = int(input())
c = [[0 for _ in range(N+1)] for _ in range(N+1)] 
checked = [0 for _ in range(N+1)]
def dfs(user,visited):
    print(user, visited)
    for i in range(1,len(c[user])+1):
        if c[user][i] == 1:
            if visited[i]:continue # 현재 user의 입장에서 visited를 체크하기 위해 visited를 항상 선언한다.
            visited[i] = 1 
            if checked[i] == 0 or dfs(i, visited):
                checked[i] = user
                return True
    return False
for i in range(M):
    start ,end = map(int, input().split(' '))
    c[start][end] = 1

for i in range(1,N+1):
    visited = [ 0 for _ in range(N+1)]
    dfs(i, visited= visited)
print(*c)
print(*checked)