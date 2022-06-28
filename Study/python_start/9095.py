import sys 

T = int(input())
def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n > 3:
        return sol(n-1) + sol(n-2) + sol(n-3)
    else:
        return 0 

for i in range(T):
    num = int(input())
    print(sol(num))