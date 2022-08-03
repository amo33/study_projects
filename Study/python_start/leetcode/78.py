# def subsets(nums):
#     result_list =[]
#     flag = len(nums)
#     nums = sorted(nums)
#     def check(val, current):
#         for value in current:
#             if val <= value:
#                 return False 
#         return True 
#     def dfs(idx, current=[]):
#         if len(current) <= flag:
#             result_list.append(current)
#             if len(current) == flag:
#                 return 
#         for i in range(idx, flag):
#             if check(nums[i],current):
#                 dfs(i, current+[nums[i]])
#     dfs(0)
#     return result_list 

# nums = [4,1,0]
# print(subsets(nums))

def subsets(nums):
    result_list =[]
    flag = len(nums)
    nums = sorted(nums)
    # def check(val, current):
    #     for value in current:
    #         if val <= value:
    #             return False 
    #     return True 
    def dfs(idx, current=[]):
        result_list.append(current)
            
        for i in range(idx, flag):
            # if check(nums[i],current):
                dfs(i+1, current+[nums[i]])
    dfs(0)
    return result_list 

nums = [1,2,3]
print(subsets(nums))