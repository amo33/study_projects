import sys

def find_alternative(pre, total):
    for n in matrix[total]:
        if n == 1:
            return 1

    for n in matrix[total]:
        
        if n == pre:
            continue
        else:         
            if find_alternative(total,n) == 1:
                return 1

    return -1

def find_parent(total):
    for i in range(2,total+1):
        for n in matrix[i]:
            if n == 1:
                check[i] = 1
                break
        if check[i] == 0:
            for n in matrix[i]:    
                if(find_alternative(i,n) == 1):
                    check[i] = n


input = sys.stdin.readline


A = int(sys.stdin.readline())
check = [0] * (A+1)
matrix = [[] for j in range(A+1)]
for i in range(A-1):
    lnode, rnode = map(int, input().split())
    matrix[lnode].append(rnode)
    matrix[rnode].append(lnode)
check[1] = 1

find_parent(A)

for i in range(2, A+1):
    print(check[i])
