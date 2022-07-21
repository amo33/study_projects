# import sys 
# from itertools import permutations, combinations


# def solution(distance, rocks, n):
#     # print(list(combinations(rocks,n)))
#     options = list(combinations(rocks,n)) 
#     result_lst = []
#     for i in range(len(options)):
#         result_lst.append(check_distance(distance,rocks,options[i]))
#     return max(result_lst)

# def check_distance(distance, rocks,key_dict):
#     option_lst = set(key_dict)
#     # print(option_lst)
#     rocks = sorted(rocks)
#     dist_lst = []
#     pre = 0
#     flag = 0
#     for lst in rocks[:]:
#         if lst in option_lst:
#             rocks.remove(lst)

#     for j in range(len(rocks)+1):
#         if j != len(rocks):
#             dist_lst.append(rocks[j] - pre)
#             pre = rocks[j] 
#         elif j == len(rocks):
#             dist_lst.append(distance - rocks[j-1])
#         flag +=1
#     # print(dist_lst)
#     return min(dist_lst)
# distance = 25 
# rocks = [2, 14, 11, 21, 17] 
# n = 2 
# print(solution(distance, rocks, n))


# import sys 
# from itertools import permutations, combinations


# def solution(distance, rocks, n):
#     rocks_options = [i for i in range(len(rocks))]
#     options = list(combinations(rocks_options,n)) 
#     basic_map = []
#     rocks = sorted(rocks)
#     pre = 0 
#     for j in range(len(rocks)+1):
#         if j != len(rocks):
#             basic_map.append(rocks[j] - pre)
#             pre = rocks[j] 
#         elif j == len(rocks):
#             basic_map.append(distance - rocks[j-1])
#     # print(basic_map)
#     result_lst = []

#     for i in range(len(options)):
#         result_lst.append(check_distance(basic_map,rocks,options[i],distance))
#     # print(result_lst)
#     return max(result_lst)

# def check_distance(distance_lst, rocks,eliminate_rock,max_dist):
    
#     for i in range(len(eliminate_rock)):
#         max_dist = min(binary_search(distance_lst, eliminate_rock[i], 0, len(rocks)), max_dist)
#     return min(max_dist)
# def binary_search(distance_lst, rock,start,end):
#     mid = (start+end)//2
#     if mid == rock:
#         return distance_lst[rock][rock-1]
# distance = 25 
# rocks = [2, 14, 11, 21, 17] 
# n = 2 
# print(solution(distance, rocks, n))


import sys 
from itertools import permutations, combinations


def solution(distance, rocks, n):
    
    answer = 0
    rocks = sorted(rocks)
    pre = 0 
    end = distance 
    while pre <= end:
        mid = (pre+end)//2 
        eliminate = 0 
        start_stone = 0
        for rock in rocks:
            if rock - start_stone < mid: # 제거해야할 값이 더 크다면 돌 제거 +1 
                eliminate +=1 
            else:
                start_stone = rock # 그게 아니라면 현재 시작 돌을 새로 업데이트한다.
            if eliminate > n: # 만약 돌 개수가 적정을 넘기면, distance를 너무 크게 잡고 있는거다.
                break 
        if eliminate > n:
            end = mid -1 # distance인 mid를 더 작게 구한다. 
        else: # 그게 아니라면 적정 개수에 맞게 구했으니
            answer = mid # 정답 후보로 넘겨주고, 
            pre = mid+1 #mid+1로 길이를 구해보자. 
        print(answer, pre, end, start_stone)
    return answer

distance = 25 
rocks = [2, 14, 11, 21, 17] 
n = 2 
print(solution(distance, rocks, n))