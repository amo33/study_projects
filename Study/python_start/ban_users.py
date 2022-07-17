# # 해당 문제는 불량 사용자 라는 프로그래머스 문제다 .
# import sys 
# from itertools import product
# def solution(user_id, banned_id):
#     #banned_check = set(banned_id_raw)
#     #banned_id = list(banned_check)
#     option_lst = []
#     for i in range(len(banned_id)):
#         option_lst.append([])
#     for i in range(len(banned_id)):
#         for j in range(len(user_id)):
#             if len(banned_id[i]) == len(user_id[j]):
#                 flag = 0
#                 if check_joker(user_id) == len(banned_id[i]):
#                     option_lst[i].append(user_id[j])
#                     continue
#                 for k in range(len(user_id[j])):
#                     if user_id[j][k] != banned_id[i][k] and banned_id[i][k] != '*':
#                         flag =1 
#                         break 
#                 if flag == 0:
#                     option_lst[i].append(user_id[j])
#     # print(option_lst)
#     product_lst = list(product(*option_lst))
#     # check_result = 0 
#     set_lst = set()
#     for lst in product_lst:
#         check_lst = set(sorted(lst))
#         # print("checking",check_lst, lst)
#         if len(check_lst) == len(lst):
#             if tuple(check_lst) in set_lst:
#                 print(1)
#                 continue
#             # check_result +=1
#             # print("status",set_lst)
#             set_lst.add(tuple(check_lst))

#     # print(product_lst)
#     return len(set_lst)
# def check_joker(p):
#     lst = [0 for i in range(len(p)) if p[i] == '*']
#     return len(lst)

# user_lst = ["aaaaaaaa", "bbbbbbbb", "cccccccc", "dddddddd", "eeeeeeee", "ffffffff", "gggggggg", "hhhhhhhh"]
# banned_id = ["********","********","********","********","********","********","********","********"]
# # user_lst = list(sys.stdin.readline().strip().split())
# # banned_id = list(sys.stdin.readline().strip().split())
# print(solution(user_lst, banned_id))

#정규 표현식 공부
# https://whatisthenext.tistory.com/116
import re ,sys
from itertools import permutations
def solution(user_id, banned_id):
    #banned_check = set(banned_id_raw)
    #banned_id = list(banned_check)
    check_lst = list()
    option_lst = list(permutations(user_id,len(banned_id)))
    for lst in option_lst:
        count = 0
        for i in range(len(banned_id)):
            check = re.compile(f"^{banned_id[i].replace('*','.')}$") # ban해야하는 문자열을 정규표현식으로 변경시 *는 반복을 의미하므로 replace해준다.
            print(check)
            flag = check.match(lst[i])
            if flag and len(banned_id[i]) == flag.end(): # if there is a match and the length is the same -> then true it is.
                count +=1 
        if count == len(banned_id): # if we get the number of id 's make as list and append 
            temp_lst = sorted(list(map(str,lst)))
            check_lst.append(temp_lst)
    answer = set(map(tuple,check_lst)) # and then set this as tuple 
    return len(answer)
user_lst = ["aaaaaaaa", "bbbbbbbb", "cccccccc", "dddddddd", "eeeeeeee", "ffffffff", "gggggggg", "hhhhhhhh"]
banned_id = ["********","********","********","********","********","********","********","********"]
user_lst = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
# user_lst = list(sys.stdin.readline().strip().split())
# banned_id = list(sys.stdin.readline().strip().sp?lit())
print(solution(user_lst, banned_id))