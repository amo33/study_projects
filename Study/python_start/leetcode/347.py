import collections 

def topKFrequent(nums, k: int):
    common_list = collections.Counter(nums).most_common(k)
    print([val for val,cnt in common_list])

lst = [1,1,1,2,2,3]
k = 2
topKFrequent(lst, k)