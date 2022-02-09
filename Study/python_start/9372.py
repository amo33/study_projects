import sys

input = sys.stdin.readline

def dfs(node, cnt):
    check[node] = 1
    for n in range(node, country+1):
        if check[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt 

test_case = int(sys.stdin.readline())

for i in range (0,test_case):
    country , plane = map(int, input().split())
    matrix = [[0 for col in range(country+1)] for row in range(country+1)]
    for j in range(plane):
        conA, conB = map(int, input().split())
        matrix[conA][conB] = 1
        matrix[conB][conA] = 1
    check = [0] * (country + 1)
    check[0] = 1
    cnt = dfs(1,0)
    print(cnt)
