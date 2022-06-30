import sys 

val , p = map(int, input().split(' '))
result_lst = []
result_lst.append(val)
while True:
    total_len = len(str(val))
    ten = 10
    sum_value = 0
    for i in range(total_len-1,-1,-1):
        num = int(str(val)[i])
        sum_value += num ** p 
        # val -= int(num * ten / 10)
        # ten *= 10
    if sum_value in result_lst:
        idx = result_lst.index(sum_value)
        result_lst = result_lst[:idx]
        break
    else:
        result_lst.append(sum_value)
        val = sum_value
print(len(result_lst))
