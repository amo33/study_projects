import sys 
N = int(input())
sharks = [[] for _ in range(N+1)] # 상어들중 자기가 잡아먹을 수 있는 정보를 모은다. 
target_lst = []
for i in range(N):
    target_lst.append(list(map(int, input().split(' ')))) 
# print(target_lst)
for i in range(N):
    for j in range(N):
        if i !=j:
            if target_lst[i][0] >= target_lst[j][0] and target_lst[i][1] >= target_lst[j][1] and target_lst[i][2] >= target_lst[j][2]:
                if i+1 in sharks[j+1]:
                    continue
                sharks[i+1].append(j+1)
# print(sharks)
# 정보 정리


checked = [0 for _ in range(N+1)]
def shark_track(val, eaten):
    for i in range(len(sharks[val])):
        trace = sharks[val][i]
        if eaten[trace]: continue 
        eaten[trace] = 1
        if (checked[trace] == 0 or shark_track(checked[trace], eaten)):
            checked[trace] = val 
            return True
    return False 
for j in range(2):
    for i in range(1, N+1):
        eaten = [0 for _ in range(N+1)]
        # if checked[i] != 0:
        #     continue 
        shark_track(i, eaten)

X = [0 for x in checked[1:] if x == 0]
# print(checked)
# print(X)
print(len(X))