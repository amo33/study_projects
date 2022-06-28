import sys 
lst =[]
INF = 100000

lst.append([0, 5, INF, 8])
lst.append([7, 0, 9, INF])
lst.append([2, INF, 0, 4])
lst.append([INF, INF, 3, 0])

for k in range(4):
    for i in range(4):
        if k != i:
            for j in range(4):
                if lst[i][j] > lst[i][k] + lst[k][j]:
                    lst[i][j] = lst[i][k] + lst[k][j]
print(*lst)