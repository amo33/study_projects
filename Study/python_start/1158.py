import sys 
from collections import deque 
N, k = map(int, input().split(' '))
visited = [0 for _ in range(N+1)]
front = deque([str(i) for i in range(1, N+1)])
back = deque()
result_lst = deque()
idx = 0
sum_val = 0
front_length = len(front)
back_length = len(back)
total_length = 0

while True:
    
    idx += k
    total_length = back_length+ front_length
    if total_length == 0:
        break
    # print(total_length, front_length, back_length)
    idx %= total_length 
    if idx == 0:
        idx = total_length

    if front_length > idx:
        # print("f",idx)
        for i in range(front_length - idx):
            back.appendleft(front.pop())
            front_length -=1
            back_length +=1
        result_lst.append(front.pop())
        front_length -=1
        # print(front_length, back_length)
        sum_val+=1
        # print(front)
        # print(back)
        # print(result_lst)
    elif front_length < idx:
        # print("b",idx)
        for i in range(idx - front_length-1):
            front.append(back.popleft())
            back_length-=1
            front_length+=1
        result_lst.append(back.popleft())
        back_length -=1
        # print(front_length, back_length)
        sum_val+=1
        # print(front)
        # print(back)
        # print(result_lst)
    else:
        result_lst.append(front.pop())
        front_length -=1
        sum_val +=1
        # print(front_length, back_length)
        # print(front)
        # print(back)
        # print(result_lst)
    idx -=1
# while front:
#     result_lst.append(front.popleft())
# while back:
#     result_lst.append(back.popleft())
# print(result_lst)
print("<",', '.join(result_lst),">",sep='')