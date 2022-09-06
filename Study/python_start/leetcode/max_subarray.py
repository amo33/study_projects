class Solution:
    def maxSubArray(self, nums) -> int:
        flag1 = flag2 =nums[0]
        
        for i in range(1, len(nums)):
            flag1 = max(flag1+nums[i],nums[i])
            flag2 = max(flag1, flag2)
        
        return flag2