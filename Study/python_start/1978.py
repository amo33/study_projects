import sys , math 
N = int(input())
lst = list(map(int, sys.stdin.readline().strip().split())) # 이중에서 소수 개수 추출 
#val = max(lst)
cnt = 0
for val in lst:
    if val != 1:
        flag = 1
        standard = math.floor(val **0.5) 
        for j in range(2,standard+1):
            if val % j == 0:
                flag = 0
                break 
        if flag == 1:
            cnt += 1
print(cnt)