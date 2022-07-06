import sys 
from itertools import combinations
T = int(input())
def gcd(a,b):
    while a > 0:
        r = a%b 
        if r == 0:
            return b 
        else:
            a = b 
            b = r
for i in range(T):
    lst = list(map(int,sys.stdin.readline().strip().split()))[1:] 
    # print(lst)
    combin_lst = list(combinations(lst,2))
    result = 0
    for pair in combin_lst:
        # print(pair)
        result += gcd(pair[0], pair[1])
    print(result)
    