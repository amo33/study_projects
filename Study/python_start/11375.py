import sys 
N, M = map(int, input().split(' '))
lst = [[] for _ in range(N+1)]
stored = [0 for _ in range(M+1)] #실제 일 배정 저장 공간 
def biparitie(val, visited):
    global cnt
    #print(lst[val])
    for i in range(len(lst[val])):
        store = lst[val][i]
        
        if visited[store] == 1: continue
        #print(store)
        visited[store] = 1
        if stored[store] == 0 or biparitie(stored[store], visited):
            #print("stored",stored)
            stored[store] = val 
            #print(stored)
            return True # true 반환!~
    return False # false 반환! 
        
for i in range(1,N+1):
    lst[i] = list(map(int, sys.stdin.readline().split(' ')))[1:] # 여러 개 받아온다.
for i in range(1,N+1):
    visited = [-1 for _ in range(M+1)] # visited는 현재 들어오는 일을 기준으로 재기에 새로운 일마다 초기화
    biparitie(i, visited)

X = [i for i in stored if i != 0]
print(len(X))
