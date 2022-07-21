from collections import deque 
def trap(height):
    volume = 0
    if len(height) == 0:
        return volume 
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    while left < right:
        left_max , right_max = max(left_max, height[left]), max(right_max, height[right])
        if left_max < right_max:
            volume += left_max - height[left]
            left+=1 
        elif left_max >= right_max:
            volume+= right_max - height[right]
            right -=1 
        
    return volume 
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))