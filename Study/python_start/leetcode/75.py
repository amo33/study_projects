def denmarkflag(listofnum, mid)-> list:
    i, j , right = 0, 0, len(listofnum)
    while j < right:
        if listofnum[j] < mid:
            listofnum[i] , listofnum[j] = listofnum[j], listofnum[i]
            i+=1
            j+=1 
        elif listofnum[j] > mid:
            right -=1 # since I decided to define right starting from len(listofnum)
            listofnum[j] , listofnum[right] = listofnum[right] , listofnum[j]
        else:
            j+=1 
    return listofnum

nums = [2,0,2,1,1,0]
mid = int(sum(nums)// len(nums))
print(denmarkflag(nums, mid))