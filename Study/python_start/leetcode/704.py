def search(nums, target: int) -> int:
        index = len(nums)//2
        left= 0 
        right = len(nums) -1 
        # if left==right:
        flag = False
        while left<=right:
            print(left,right)
            mid = int(left+right)//2
            if flag: # flag 1이면 이미 한 번 left, right 같은걸 체크한것이므로 자동으로 return -1
                return -1
            if left==right: # 만약 left==right이면 나중에 값 못 찾을거 대비해서 flag=True로 둔다. 
                flag=True
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target: # 현재 범위보다 좁혀야한다. 
                right = mid 
            elif nums[mid] < target:
                left = mid+1 

        return -1