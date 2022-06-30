import sys 
import collections 
N = int(input())
arr= {}
for i in range(N):
    val = int(input())
    if val in arr.keys():
        pass 
    else:
        arr[val] = 0
    arr[val]+=1 
od = collections.OrderedDict(sorted(arr.items()))
print(max(od, key = od.get))
# max_key = max(arr, key = arr.get) 
# key값으로 들어온 arr.get은 보통 arr.get(<key>)가 들어와서 value가 나온다. 즉, value 중 기준으로 max를 출력한다는 뜻 

# [k for k,v in di.items() if max(di.values()) == v]
# 이 방식은 max 값을 가진 모든 key value들을 반환해준다. 
# 위에 방식인 arr.get과 이 방식의 차이는 max_key는 한 개만 출력해준다.
#print([k for k, v in arr.items() if max(arr.values())== v])