import collections 

def lengthOfLongestSubstring(s: str) -> int:
    max_cnt = 0 
    # max_string = ''
    p1 = 0
    p2 = 0
    while True:
        if p2 > len(s) -1:
            
            break  
        p2 +=1 
        if p2 - p1 != len(set(s[p1:p2])): # if no duplicate
            p2 -=1
            if max_cnt < p2 - p1:
                # max_string = s[p1:p2]
                max_cnt =  p2 - p1 
            # print(max_string, p2, p1)
            p1 +=1 
            p2 = p1
    if max_cnt < p2 - p1:
        # max_string = s[p1:p2]
        max_cnt =  p2 - p1 
    # print(max_string)
    return max_cnt 

# print(lengthOfLongestSubstring(" "))

def lengthOfLongestSubstring2(s: str) -> int:
    max_cnt = 0 
    queue = collections.deque()

    for i in range(len(s)):
        if s[i] in queue:
            max_cnt = max(max_cnt, len(queue))
            while True:
                if queue.popleft() == s[i]:
                    break
            queue.append(s[i])

        else:
            queue.append(s[i])
    max_cnt = max(max_cnt, len(queue))
    return(max_cnt)

print(lengthOfLongestSubstring2("bbbbb"))
