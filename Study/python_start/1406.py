# import sys 
# from collections import deque
# # string_input = [' '] * 600000
# # print(len(string_input))
# # string_input = deque(sys.stdin.readline().rstrip('\n'))
# string_input = sys.stdin.readline().rstrip('\n')
# idx = len(string_input)
# total_input = len(string_input)
# num = int(input())
# def erase(total_input , idx, string_input):
#     if idx == 0:
#         return total_input, idx, string_input
#     else:
#         total_input -=1
#         front_space = deque(string_input[:idx])
#         back_space = deque(string_input[idx:])
#         front_space.pop()
#         idx -=1 
#         # print("{b",idx)
#         # string_input_result = ''.join(front_space, back_space)
#         front_space += back_space 
#         string_input_result = ''.join(front_space)
#         return total_input,idx, string_input_result
# def add_char(idx, val, string_input, total_input):
#     if idx == total_input:
#         string_input_result = ''.join([string_input,val])
#         # front_space += back_space 
#         # string_input_result = ''.join(front_space)
#     else:    
#         front_space = deque(string_input[:idx])
#         back_space = deque(string_input[idx:])
#         front_space.append(val)
#         front_space += back_space 
#         string_input_result = ''.join(front_space)
#         # string_input_result = ''.join([front_space, back_space])

#     return string_input_result
# for i in range(num):
#     try:
#         input_option = sys.stdin.readline().rstrip('\n').split(' ')
#         option, val = input_option[0], input_option[1]
#     except:
#         option = input_option[0]
#     finally:
#         if option == 'B':
#             total_input , idx, string_input = erase(total_input , idx, string_input)
#             # print(string_input[:10])
#         elif option == 'L':
#             if idx > 0:
#                 idx -=1 
#         elif option == 'D':
#             if idx < total_input:
#                 idx +=1 
#         elif option == 'P':
#             string_input = add_char(idx, val, string_input, total_input )
#             total_input += 1
#             idx +=1

# print(''.join(string_input))
# # for i in range(len(string_input)):
# #     if string_input[i] ==' ':
# #         break
# #     else:
# #         print(string_input[i],end="")

# import sys

# front= list(sys.stdin.readline().rstrip())
# back = []

# for _ in range(int(sys.stdin.readline())):
# 	option = list(sys.stdin.readline().split())
#     if option[0] == 'L':
# 		if front:
#         	back.append(front.pop())
            
# 	elif option[0] == 'D':
#     	if back:
#         	front.append(back.pop())

# 	elif option[0] == 'B':
#     	if front:
#         	back.pop()
            
# 	else:
#     	front.append(option[1])
        
# front.extend(reversed(back))
# print(''.join(front))

import sys 
front = list(sys.stdin.readline().rstrip())
back = []

for _ in range(int(sys.stdin.readline())):
    option = list(sys.stdin.readline().split()) # 그냥 공백 split 
    if option[0] == 'L':
        if front:
            back.append(front.pop())
    elif option[0] == 'D':
        if back:
            front.append(back.pop())
    elif option[0] == 'B':
        if front:
            front.pop()
    else:
        front.append(option[1])
front.extend(reversed(back))
print(''.join(front))