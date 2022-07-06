import sys 

input_string = sys.stdin.readline().strip()
i = 0
result_lst = [-1 for _ in range(26)]
while i < len(input_string):

    idx = ord(input_string[i])-97
    # print(idx)
    # print(result_lst[idx])
    if result_lst[idx] == -1:
        result_lst[idx] = i
    i +=1
print(*result_lst)
