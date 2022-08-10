import heapq
def search( nums, target) -> int:
        def getindex(nums, target):
            # min_value = min(nums)
            mid= 0
            tree = []
            for i, num in enumerate(nums):
                heapq.heappush(tree, (i, num))
                # print(tree)
            min_value = float('inf')
            result_index = -1
            while tree:
                index, num = heapq.heappop(tree)
                if min_value > num:
                    mid = index 
                    min_value = num 
                if num == target:
                    result_index = index 
     
            # pivot = len(nums) - mid
            # print(pivot,mid,target)
            # index = mid + target - min_value if target <= nums[0] else target - pivot -1 
            return result_index
        num_set = set(nums)
        # print(num_set)
        
        if target not in num_set:
            # print("2")
            return -1 
        else:
            # print("1")
            return getindex(nums,target)