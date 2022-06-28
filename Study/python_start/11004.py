import sys 
N, k = map(int , input().split(' '))
lst = list(map(int, sys.stdin.readline().split(' ')))
print(sorted(lst)[k-1])