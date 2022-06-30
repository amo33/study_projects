import sys 

N = int(input())

val_lst = list(input()) # 문자열 자체를 입력받았을때 다 자르는 방법 
sum = 0
for i in range(N):
    sum +=int(val_lst[i])
print(sum)