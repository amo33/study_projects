def combine( n: int, k: int): # 8292ms too slow than I expected,,! 
    def check(val, list):
        for value in list:
            if value >= val:
                return False 
        return True 
    
    result_list = []
    nums = range(1,n+1)
    def dfs(nums,cnt,current_list=[]):
        if cnt == k:
            result_list.append(current_list)
            return 
        for num in nums:
            if check(num, current_list):
                dfs(nums,cnt+1, current_list+[num])
        
    dfs(nums,0)
    return result_list 

n = 4 
k = 2
print(combine(n,k))

def combine( n: int, k: int): # 8292ms too slow than I expected,,! 
    def check(val, list):
        for value in list:
            if value >= val:
                return False 
        return True 
    
    result_list = []
    nums = range(1,n+1)
    def dfs(nums,flag,cnt,current_list=[]):
        if cnt == k:
            result_list.append(current_list)
            return 
        for i in range(flag,len(nums)):
            if check(nums[i], current_list):
                dfs(nums,i+1,cnt+1, current_list+[nums[i]])
        
    dfs(nums,0,0)
    return result_list 