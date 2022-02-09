import sys

input = sys.stdin.readline

N, M = map(int, input().split())

rectangular = list()

for i in range(N):
    rectangular.append(input().rstrip("\n"))

repair = list()

for i in range(N-7):
    for j in range(M-7):
        first_w = 0
        first_b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) %2 == 0:
                    if rectangular[k][l] != 'W':
                        first_w = first_w + 1
                    if rectangular[k][l] != 'B':
                        first_b = first_b + 1
                else:
                    if rectangular[k][l] != 'B':
                        first_w = first_w + 1
                    if rectangular[k][l] != 'W':
                        first_b = first_b + 1
        repair.append(first_w)
        repair.append(first_b)

print(min(repair))