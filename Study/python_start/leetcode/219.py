import collections 
def containsNearbyDuplicate(nums, k: int) -> bool:
        window = collections.deque()
        status = collections.defaultdict(int)
        flag = False
        for i , num in enumerate(nums):
            window.append(num)
            status[num]+=1
            if status[num] >1:
                flag = True # 하나라도 있다면 True로 해준다. for문 돌아가면서 체크할 필요가 없다.

            if i<k:
                continue

            status[window.popleft()] -=1 

        return flag