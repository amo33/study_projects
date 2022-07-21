from itertools import permutations
# def check_tree(status, j,idx,result, summation,result_lst,checked_lst,nums):
#     if status == 3:
#         temp_lst = sorted(list(map(int, result.strip().split())))
#         checked_str = str(temp_lst)
#         if summation == 0:
            
#             if checked_str in checked_lst:
#                 return 
#             else:
#                 checked_lst.add(checked_str)
#                 # print("1",checked_lst)
#                 result_lst.append(temp_lst)
#     else:
#         check_set = set(list(map(int, idx.strip().split())))
#         for k in range(j, len(nums)):
#             if k in check_set:
#                 continue
#             check_tree(status+1, k+1,idx+' '+str(k), result+' '+str(nums[k]), summation + nums[k],result_lst,checked_lst, nums)
        



# def check_tree(nums,checked):
#     option_lst = list(permutations(nums,3))
#     result_lst = []
#     for i in range(len(option_lst)):
#         # print(option_lst)
#         if sum(option_lst[i]) == 0:
#             # print(set(tuple(sorted(option_lst[i]))), checked)
#             if tuple(sorted(option_lst[i])) in checked:
#                 continue
#             result_lst.append(option_lst[i])
#             checked.add(tuple(sorted(option_lst[i])))
#     return result_lst
        
# def threeSum(nums):
#     result_lst = []
#     check_lst = set()
#     nums = sorted(nums)
#     result_lst = check_tree(nums,check_lst)
#     return result_lst

def threeSum(nums):
    result_lst = []
    nums = sorted(nums)
    for i in range(len(nums)):
        # if i>0 and nums[i] == nums[i-1]: # 이전에 체크한 결과들을 두번이상 정답으로 간주하지 않게 하기 위해 쓰인다.
        #     continue
        left = i+1
        right = len(nums) -1 
        while left < right:
            target = nums[i]
            if nums[left] + nums[right] + target > 0:
                right -=1 
            elif nums[left]+ nums[right] + target < 0:
                left+=1 
            elif nums[left] + nums[right] + target ==0:
                result_lst.append([nums[i], nums[left], nums[right]])
                print(nums[i],nums[left],nums[right])
                while left < right and nums[left]==nums[left+1]:
                    left +=1 
                while left<right and nums[right-1] == nums[right]:
                    right -=1
                left +=1 
                right -=1
    return result_lst           

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))