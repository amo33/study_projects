# import sys 
# from itertools import combinations

# def extractproduct(*args):
#     lst = args
#     # print("f",lst)
#     product = 1
#     for val in lst:
#         product *= val 
#     if product % 10 == 0:
#         return True 
#     return False 

# N, M = map(int , sys.stdin.readline().strip().split())
# num_total_list = [i+1 for i in range(N)]
# combination_lst = list(combinations(num_total_list,M))
# cnt = 0 
# for lst in combination_lst:
#     # print(lst)
#     if extractproduct(*lst) == True:
#         cnt +=1 
# print(lst)

import sys 

N, M = map(int , sys.stdin.readline().strip().split())
def factorial(val):
    if val == 0:
        return 1
    return factorial(val-1) * val 
val =factorial(N)/(factorial(N-M)*factorial(M))

cnt = 0
while True:
    if val % 10**(cnt+1) == 0:
        cnt +=1
    else:
        break 
print(cnt)