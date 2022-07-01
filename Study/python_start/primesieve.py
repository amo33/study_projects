import sys 

val = int(input())

num_lst = [i for i in range(val+1)]


for i in range(2,val+1):
    if num_lst[i] ==0:
        continue 
    for j in range(i*2, val+1): # need to remember that for loop starts at the multiple of i ==> i*2
        if num_lst[j] % i == 0:
            if num_lst[j] != i:
                num_lst[j] = 0  #before removal change remove num all to 0 

remove_set = {0}
result_lst = [i for i in num_lst if i not in remove_set]

print(result_lst)