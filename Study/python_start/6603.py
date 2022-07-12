# import sys 
# from itertools import combinations
# idx = False 
# while True:
#     input_string = list(map(int,sys.stdin.readline().strip().split()))
#     if input_string[0] == 0:
#         break 
#     if idx != False:
#         print()
#     else:
#         idx = True
#     lst_options = list(combinations(input_string[1:], 6))
#     for i in range(len(lst_options)):
#         print(*lst_options[i])

import sys 
idx = False 

def generate_num(lst,total_cnt,pre,result):
    if total_cnt == 6:
        print(* result)
        return

    for i in range(pre,len(lst)):
        # print(i)
        # if lst[i] not in result: 
        result.append(lst[i])
        generate_num(lst,total_cnt+1,i+1,result)
        result.pop()

while True:
    input_string = list(map(int,sys.stdin.readline().strip().split()))
    if input_string[0] == 0:
        break 
    if idx != False:
        print()
    else:
        idx = True
    # print("1",input_string[1:])
    generate_num(input_string[1:], 0,0,[])