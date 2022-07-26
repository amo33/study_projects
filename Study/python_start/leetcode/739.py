import collections 
temperatures = [89,62,70,58,47,47,46,76,100,70]
visited = [0] * len(temperatures)
stack = collections.deque()
for i in range(len(temperatures)):
    print(stack)
    if stack and stack[-1][0] >= temperatures[i]:
        stack.append([temperatures[i], i])
        continue
    while stack:
        if stack[-1][0] >= temperatures[i]:
            break 
        elif stack[-1][0] < temperatures[i]:
            val,idx = stack.pop()
            visited[idx] = i - idx 
        
    stack.append([temperatures[i], i])
print(visited)