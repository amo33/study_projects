'''import sys 

input = sys.stdin.readline

lines = int(input())

lst = []

for i in range(lines):
    val = int(input())
    lst.append(val)

count = [0] * (max(lst)+1)

for i in range(lines):
    count[lst[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
'''
# 위 방식은 메모리 에러 난다. 기본적인 정렬 중 가장 빠른 걸 선택해 보자. 
# 8MB 여서 정말 적은 메모리이기에 일반적인 정렬은 안된다.
import sys 

input = sys.stdin.readline

lines = int(input())

lst = [0] * 10001
for i in range(lines):
    val = int(input())
    lst[val] +=1

for i in range(10001):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)

