import sys 
N = int(input())
name_lst = []
for i in range(N):
    name ,language, english, math = input().split(' ')
    language, english, math = int(language) , int(english) , int(math)
    name_lst.append([name, language, english, math])

for val in sorted(name_lst,key=lambda x: (-x[1], x[2], -x[3], x[0])):
    print(val[0])