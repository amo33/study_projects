import heapq 
def findKthLargest( nums, k: int) -> int:
        queue = []
        value = -1
        # for num in nums: # option 1 : code line 5 ~ 9 -> convert list to heap and pop it for k times  
            # heapq.heappush(queue, (-num,num))
        # for _ in range(k):
            # _ ,value = heapq.heappop(queue)
        # return value
        
        # option 2 : use heapify to convert list to heap without pushing and pop until k th. 
        # heapq.heapify(nums) # using heapify helps me not to use pushing operation for n times to convert list to heap
        # for _ in range(len(nums) - k):
        #     heapq.heappop(nums)
        # return heapq.heappop(nums)
        return heapq.nlargest(k,nums)[-1] # useful method but relative time consumption much more .
        