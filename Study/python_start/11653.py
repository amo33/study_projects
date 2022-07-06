import sys, math 
N = int(input())
board = [1] * (N+1) 
val = math.floor(N**0.5)
board[0], board[1] = 0, 0
for i in range(2, N+1):
    for j in range(2, val+1):
        if i!=j and i % j ==0:
            board[i]= 0 
            break 
primes = [i for i,j in enumerate(board) if j]
# print(primes)
index = 0
while N >1:
    while N % primes[index] == 0:
        print(primes[index])
        N //= primes[index]
        # print(N)
    index +=1