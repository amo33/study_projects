import sys , heapq ,re

que = []
input_string = sys.stdin.readline().strip()
lst = list(map(int,re.split('[+-]',input_string)))
idx = 0
cnt = 0
idx_lst = [0]
for i in input_string:
    if i == '-':

        cnt+=1
        idx +=1 
        idx_lst.append(idx)
    elif i == '+':

        cnt+=1
        idx +=1 
idx_lst.append(len(lst))
temp = 0
first = True 
for i in range(1,len(idx_lst)):
    temp_temp = 0
    for j in range(idx_lst[i-1],idx_lst[i]):
        temp_temp += lst[j]
    if first == True :
        first = False 
        temp += temp_temp
    else:
        temp -= temp_temp
print(temp)