import itertools
def permute(nums):
    def check(val, str_list):
        for value in str_list:
            if value == val:
                return False 
        return True 
    result_list = []
    def permutations(nums, result_string):
        if len(result_string) == len(nums):
            
            result_list.append(result_string)
            return 
        for num in nums:
            if check(num, result_string):
                permutations(nums, result_string+[num])
    permutations(nums, [])
    return result_list 
def permute2(nums):
    return list(map(list,itertools.permutations(nums)))
nums = [0,-1,1]
print(permute(nums))
