'''import sys 

N, K = map(int, input().split(' '))
lst = []
for i in range(N):
    lst.append(int(input()))
cnt = 0
lst = sorted(lst, reverse=True)
for i in range(N):
    if K == 0:
        break
    if K >= lst[i]:
        cnt += K // lst[i]
        K = K % lst[i]
print(cnt)'''
import sys 

N, K = map(int, input().split(' '))
lst = []
for i in range(N):
    lst.append(int(input()))
cnt = 0

for i in range(N-1, -1, -1): # (시작, 끝에보다 +1 , 방식(forward, backward))
    print("=================")
    print(lst[i])
    if K == 0:
        break
    if K >= lst[i]:
        print(K)
        cnt += K // lst[i]
        K = K % lst[i]
        print(K)
print(cnt)