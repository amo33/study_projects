import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방


def dfs(x):
    global result
    visited[x] = 1
    cycle.append(x)
    number = numbers[x] # 간선 활용 
    
    if visited[number]: 
        if number in cycle: 
            result += cycle[cycle.index(number):]  # 현재까지를 합한다.
        return
    else:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [1] + [0] * N 
    result = []
    
    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            dfs(i)
            
    print(N - len(result))