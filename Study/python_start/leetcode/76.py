import collections
def minWindow( s: str, t: str) -> str:
        num = collections.Counter(t)
        missing = len(t) 
        
        left = start =end=0 
        for right ,char in enumerate(s,1):
            missing -= num[char] > 0
            num[char] -= 1
            if missing == 0:
                while left < right and num[s[left]]<0:
                    num[s[left]]+=1
                    left+=1
                # print(num)
                if not end or right - left < end - start:
                    start ,end = left, right 
                    num[s[left]]+=1 
                    missing +=1 #left가 찾아야하는 문자 중 하나여서 missing +1
                    left +=1 # 한칸 더 옮긴다. 왜냐하면 해당 left 값은 missing 중 한 값이기 때문에 다음 index로 넘겨야한다.
                    print(start,end)
                    print(left,right,num)
        return s[start:end]