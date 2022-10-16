def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_lst = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) -1
            
            while left < right:
                if nums[left] + nums[right] + nums[i] >0:
                    right -=1
                elif nums[left] + nums[right] + nums[i] <0:
                    left +=1
                    
                else:
                    result_lst.append([nums[i],nums[left],nums[right]])
                    temp1, temp2 = left, right
                    while left < right and nums[left] == nums[left+1]:
                            left+=1 
                    while left < right and nums[right] == nums[right-1]:
                            right -=1 
                    left+=1
                    right -=1
        return result_lst