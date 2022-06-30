import sys 

N = int(input())
name_lst = []
for i in range(N):
    age , name = input().split(' ')
    age = int(age)
    name_lst.append([age, name])

for val in sorted(name_lst, key=lambda x: x[0]):
    print(val[0], val[1])