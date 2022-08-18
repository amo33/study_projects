import collections 
def characterReplacement( s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s)+1):
            counts[s[right-1]]+=1 # 값을 0 index부터 더해준다. 
            max_char = counts.most_common(1)[0][1] # 현재 가장 값이 큰 max_char를 뽑는다. 
            
            if right - left - max_char > k: # 만약 현재 k개의 길이보다 크다면, left 인덱스를 이동 
                counts[s[left]] -=1
                left+=1 
                
        return right - left 