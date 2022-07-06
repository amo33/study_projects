import sys , math
K = int(math.sqrt(1000000)) + 1
board = [1] * 1000001
board[0], board[1] = 0 , 0
for i in range(2, K):
    if board[i] == 0: continue 
    for j in range(2*i,1000001, i):
        if j > 1000000 : break 
        board[j] = False 
primes = [i for i, j in enumerate(board) if j]
primes.append(10000000000)

def siere(val):
    standard = math.floor(val**0.5)
    visited = [1] * (val+1)
    target = 0
    for i in range(2,val+1):
        for j in range(2, standard+1):
            if i % j == 0 and i!= j:
                visited[i] = 0 
        if visited[i] == 1:
            target = max(target, i)
    left_ones = [i for i in range(2,val+1) if visited[i] != 0]
    # print(left_ones)
    if val - target in left_ones:
        return target, val - target , True 
    i = 0 
    j = len(left_ones) -1
    while left_ones[i] + left_ones[j] != val:
        if left_ones[i] + left_ones[j] > val:
            j -= 1
        elif left_ones[i] + left_ones[j] < val:
            i+=1
        # print(i,j)
        if i > j:
            return 0, 0, False
    return left_ones[i], left_ones[j] , True
def binary_search(val,0,):
    if 
while True:
    val = int(input())
    if val == 0: break # 탈출 
    prime_one, prime_two, flag = siere(val)
    if prime_one > prime_two:
        prime_one , prime_two = prime_two, prime_one
    if flag == True:
        print("{} = {} + {}".format(val, prime_one, prime_two))
    elif flag == False:
        print("Goldbach's conjecture is wrong.")
