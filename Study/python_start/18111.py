
'''
import sys 

input = sys.stdin.readline

arr = [0] # 2, 1 

N, M, B = map(int, input().rstrip('\n').split(' '))
ground = []
arr[0] = B 
time = 0
sum_val = 0 
lst_time = []
lst_level = []
for i in range(N):
    ground.append(list(map(int, input().rstrip('\n').split(' '))))
    sum_val += sum(ground[i])

sum_val = round(sum_val / (N*M)) 
print(sum_val)
count = [0] * (N*M)
for i in range(N):
    for j in range(M):
        if ground[i][j] < sum_val:
            count[N*i+j] = sum_val - ground[i][j]
if arr[0] < sum(count):
    sum_val -=1

for i in range(N):
    for j in range(M):
        if ground[i][j] < sum_val:
            time += sum_val - ground[i][j]
        elif ground[i][j] > sum_val:
            time += (ground[i][j] - sum_val)*2
lst_time.append(time)
lst_level.append(sum_val)
print(count)
if arr[0] >= 2 * sum(count):
    sum_val += 1
    for i in range(N):
        for j in range(M):
            if ground[i][j] < sum_val:
                time += sum_val - ground[i][j]
            elif ground[i][j] > sum_val:
                time += (ground[i][j] - sum_val)*2
    lst_time.append(time)
    lst_level.append(sum_val)
idx = lst_time.index(min(lst_time))

print(lst_time[idx], ' ', lst_level[idx])
print(lst_time)
print(lst_level)

'''
# 평균 방식은 비효율적이다.
import sys 

input = sys.stdin.readline

 # 2, 1 

N, M, B = map(int, input().rstrip('\n').split(' '))
ground = []
inventory = B 
answer = 1000000000000000000000000000000
sum_val = 0 
for i in range(N):
    ground.append(list(map(int, input().rstrip('\n').split(' '))))
    sum_val += sum(ground[i])

for i in range(257):
    max = 0
    min = 0
    for j in range(N):
        for k in range(M):
            if ground[j][k] < i:
                min += (i - ground[j][k])
            else:
                max += ground[j][k] - i 
    inventory = max + B 
    if inventory < min:
        continue 
    time = 2*max + min 
    if time <= answer:
        answer = time 
        height = i 
print(answer, height)
