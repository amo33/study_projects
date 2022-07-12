import sys 
N = int(input())
lst = list(map(int, sys.stdin.readline().rstrip().split())) 
option_lst = list(map(int, sys.stdin.readline().rstrip().split())) 
maximum = -1e9
minimum = 1e9
def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + lst[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - lst[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * lst[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / lst[depth]), plus, minus, multiply, divide - 1)
dfs(1, lst[0], option_lst[0],option_lst[1],option_lst[2],option_lst[3])
print(maximum)
print(minimum)
