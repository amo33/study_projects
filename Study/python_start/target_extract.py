import sys 
total = 0
def backtrack(current_lst,current_idx,val,target):
    global total
    if current_idx != len(current_lst):
        backtrack(current_lst, current_idx+1, val+current_lst[current_idx], target)
        backtrack(current_lst, current_idx+1, val-current_lst[current_idx],target)
    else:
        if val == target:
            total+=1 
            
def solution(numbers, target):
    global total
    backtrack(numbers, 0, 0, target)
    answer = total
    return answer

map_lst = list(map(int, sys.stdin.readline().strip().split()))
target = int(input())
print(solution(map_lst, target))