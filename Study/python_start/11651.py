import sys 

N = int(input())
input_lst = []
for i in range(N):
    x, y = map(int, input().split(' '))
    input_lst.append([x,y])
for result in sorted(input_lst,key=lambda x: (x[1], x[0])):
    print(result[0],result[1])