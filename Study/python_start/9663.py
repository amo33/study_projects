import sys 

N = int(input())
cnt = 0
visited = [0 for _ in range(N)]
def check(idx):
    for i in range(idx):
        if visited[i] == visited[idx] or abs(idx - i) == abs(visited[i] - visited[idx]):
            return False 
    return True 
def queen_seat(n):
    global cnt
    if n == N:
        cnt +=1 
        return 
    for i in range(N):
        # print(visited, i)
        visited[n] = i 
        if check(n):
            queen_seat(n+1)
queen_seat(0)
print(cnt) 
