# from collections import deque 
# import sys 
# def solution(p):

#     answer = ''
#     left_count = 0

#     for i in range(len(p)):
#         if p[i] == '(':

#             left_count +=1 
#         elif p[i] == ')':
#             if left_count >0:
#                 left_count -=1
#             else:
#                 answer = p[0:i]
#                 answer +=text_transform(p[i:])
#                 return answer 

#     if left_count ==0:
#         answer = p
#         return answer  

# def text_transform(p):
    
#     queue = deque()
#     for i in range(len(p)):
#         if p[i] == '(':
#             queue.append(i)
#         elif p[i] == ')' and len(queue) != 0:
#             queue.pop()
#     target = '(' + solution(p[queue[-1]+1:])+ ')'
#     for i in range(1,queue[-1]):

#         if p[i] == '(':
#             target+= ')' 
#         elif p[i] == ')':
#             target+= '('

#     return target

# input_string = sys.stdin.readline().strip() 
# print(solution(input_string))

# import sys 
# def text_transform(p):
#     left_check = 0
#     right_check = 0 
#     mismatch = False 
#     idx=0
#     if p == '':
#         return p
#     for i in range(len(p)):
#         if p[i] == '(':
#             left_check +=1 
#         elif p[i] == ')':
#             right_check +=1 
        
#         if left_check < right_check:
#             mismatch = True # 개수가 왼쪽꺼보다 오른쪽것이 많다면 flag를 true로 변경 
#         elif left_check == right_check:
#             idx = i
#             break 
#     partial_string = p[:idx+1] # 현재까지 왼쪽, 오른쪽 괄호가 맞는 경우를 추출 
#     if mismatch == False: # 만약 올바른 상태면 그대로 이후 문자열 v를 호출 
#         return partial_string + text_transform(p[idx+1:])
#     elif mismatch ==True: 
#         target = '(' + text_transform(p[idx+1:]) + ')'
#         for bracket in partial_string[1:-1]:
#             if bracket == '(':
#                 target += ')'
#             elif bracket == ')':
#                 target += '('
#         # target += ')'
#         return target

# def solution(p):
#     answer =text_transform(p)
#     return answer 
# input_string = sys.stdin.readline().strip() 
# print(solution(input_string))