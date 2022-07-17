import sys


N = int(input())
checked = []
parent = [0] * (N+1)
query_store = {}
checked = [False for _ in range(N+1)]
for i in range(1,N+1):
    query_store[i] = []
for i in range(N):
    start , end , query = sys.stdin.readline().strip().split()
    query_store[start].append([end,query])
    query_store[end].append([start,query])
    #정보 저장 

def parent_find(x):
    if x == 1:
        parent[x] = 0
    else:
        parent[x] = int(x//2)
    if x*2 <= N:
        parent_find(x*2)
    if (x *2 +1) <= N:
        parent_find(x*2+1)
    
def find_diameter(x):
    if checked[x] ==False:
        checked[x] = True 
        