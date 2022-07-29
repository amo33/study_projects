def combinationSum(candidates, target: int):

    candidates = sorted(candidates)
    result_list = []
    # nums = range(1,len(candidates)+1)
    def dfs(nums,cnt,total=0,current_list=[]):
        print(current_list)
        if total == target:
            tmp = sorted(current_list)
            if tmp not in result_list:
                result_list.append(tmp)
            return
        elif cnt == target:
            # print(current_list)
            if sum(current_list) == target:
                result_list.append(current_list)
            return
        if total > target:
            return 
        for num in nums:
            # if check(num, current_list):
            dfs(nums,cnt+1, total+num,current_list+[num])
    print(candidates)
    dfs(candidates,0)
    return result_list 
num_list = [100,200,4,12]
print(combinationSum(num_list,400))
