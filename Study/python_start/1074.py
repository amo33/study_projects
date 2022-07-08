import sys 

N , r,c= map(int, sys.stdin.readline().strip().split())
if N <= 300:
    sys.setrecursionlimit(2*512)
else:
    sys.setrecursionlimit(2**N)
mid = int(2**N//2)
col = c 
row = r
cnt  = 0

def find_index(col, row, mid):
    global cnt 
    # print(mid, row, col,cnt)
    if mid == 1:
        if row == 1:
            cnt +=2 
        if col == 1:
            cnt +=1 
        return 
    elif row >= mid and col >= mid:
        cnt += 3 * mid **2
        row -= mid 
        col -= mid 
        select_max = max(row, col)
        mid = 2**(select_max // 2)
        # print(cnt)
        # print(1)
    elif row >= mid and col < mid:
        cnt += 2 * mid**2
        row -= mid 
        select_max = max(row, col)
        mid = 2**(select_max // 2)
        # print(2)
    elif row < mid and col >= mid:
        cnt += mid**2
        col -= mid 
        select_max = max(row, col)
        mid = 2**(select_max // 2)
        # print(3)
    else:
        mid //=2
    find_index(col, row, mid)
find_index(col, row, mid)    
print(cnt)
sys.exit(0)