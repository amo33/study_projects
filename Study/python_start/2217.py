import sys 
max_result = 0 
N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
while lst:
    min_val = min(lst)
    max_result = max(len(lst)*min_val,max_result)
    for i in lst[:]:
        if i == min_val:
            lst.remove(i)
print(max_result)