import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split()) 

def check(val, lst):
    
    for value in lst:
        if value == str(val):
            return False  
    return True 
def backtrack(idx,cnt,status,result_lst = ''):
    # print(idx,result_lst)
    if status == 0:
        result_lst = str(idx)
        status+=1
    if cnt == status:
        # print(result_lst)
        for val in result_lst:
            print(val, end=" ")
        print()
        return 
    
    for i in range(1,N+1):
        # print(result_lst)
        if check(i,result_lst):
            # print(result_lst)
            # visited[i] = True 
            backtrack(i+1, cnt, status+1, result_lst+str(i))
        

for i in range(1,N+1):
    # print(i,N,M)
    # visited = [False for i in range(N+1)]
    # visited[i] = True
    backtrack(i,M, 0) 
