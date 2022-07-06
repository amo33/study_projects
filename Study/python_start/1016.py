import sys , math 

start , end = map(int, input().split(' '))
visited = [0 for _ in range(end+1-start)]
squares = [i **2 for i in range(2, int(math.sqrt(end)+1))]
i =2 
cnt = 0
# print(end_max)
for sq_num in squares:
    flag = end // sq_num
    for j in range(1,flag+1):
        val = j * sq_num
        # print(i **2, j)
        if val >= start and val <= end and visited[val- start] != 1:
            visited[val- start] = 1
            cnt +=1
print(end-start+1-cnt)

# import sys , math 

# start , end = map(int, input().split())
# visited = [1 for _ in range(end+1-start)]
# squares = [i **2 for i in range(2, int(math.sqrt(end)+1))]

# for sq_num in squares:
#     val = start // sq_num * sq_num #초기 인식 숫자 체크 
#     while val < end +1 :
#         if val - start >= 0:
#             visited[val - start] = 0
#         val += sq_num
# print(sum(visited))


# mi, ma = map(int,input().split())
# a = [i**2 for i in range(2,int(ma**0.5)+1)]
# num = [1] * (ma-mi+1)
# for i in a:
#     n = mi//i*i 
#     while(n < ma+1):
#         if n - mi >= 0:
#             num[n-mi] = 0
#         n += i
# print(sum(num))