from collections import deque
import heapq 

example = [4,5,32,1,4,5,6,87,8,9,10,2,3]
# I'm going to make min heap 
heaplst = []
parent = 0 
end = len(example)

def checkheapify(index):

    parent = int(index /2) - 1 if index % 2 == 0 else int((index+1) /2) 
    
    while parent >= 0:
        print(parent)
        print(index)
        if example[parent] > example[index]:
            example[parent] , example[index] = example[index], example[parent]
        index = parent
        if parent ==0:
            break 
        if index == 1 or index == 2:
            parent = 0
        else:
            parent = int(index /2) - 1 if index % 2 == 0 else int((index+1) /2) 
    print(parent)
    print(*example)
for i in range(len(example)-1, -1, -1):
    checkheapify(i)
print(*example)    


