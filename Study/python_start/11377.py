import sys 
N, M, K = map(int, input().split(' '))
lst = [[] for _ in range(N+1)]
stored = [0 for _ in range(M+1)] #실제 일 배정 저장 공간 
def biparitie(val, visited):
    # if flag[val] == 2:
    #     return False 
    # #print(val, flag)
    # temp = flag[val]
    for i in range(len(lst[val])):
        store = lst[val][i]
        
        if visited[store] == 1: continue
        #print(val,store, stored)
        visited[store] = 1
        if stored[store] == 0 or biparitie(stored[store], visited):
            #print("stored",stored)
            stored[store] = val 
            return True # true 반환!
    return False # false 반환! 
        
for i in range(1,N+1):
    lst[i] = list(map(int, sys.stdin.readline().split(' ')))[1:] # 여러 개 받아온다.
for i in range(1,N+1):
    visited = [-1 for _ in range(M+1)] # visited는 현재 들어오는 일을 기준으로 재기에 새로운 일마다 초기화
    # flag = [0 for _ in range(N+1)] 
    biparitie(i, visited)
for i in range(1, N+1):
    visited = [-1 for _ in range(M+1)]
    if len(lst[i]) > 1 and K >0:
        if biparitie(i, visited) == True:
            K-=1
    if K <=0:
        break 

X = [i for i in stored if i != 0]
# print(lst)
# print(stored)
# print(flag)
print(len(X))
