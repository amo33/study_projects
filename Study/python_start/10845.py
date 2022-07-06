import sys 
from collections import deque 
N = int(input())

def push(x,queue):
    queue.append(x)
    # print(x)
    return queue

def size(queue):
    return len(queue)

def pop(queue):
    if size(queue) != 0:
        return queue.popleft()
    else:
        return -1 
def front(queue):
    if size(queue) != 0:
        return queue[0]
    else:
        return -1 
def back(queue):
    if size(queue) != 0:
        return queue[-1]
    else:
        return -1 
queue = deque()
for i in range(N):
    try:
        input_string = sys.stdin.readline().strip().split(' ')
        option = input_string[0]
        value = int(input_string[1])
    except:
        option = input_string[0]
    finally:
        if option == 'push':
            queue = push(value, queue)
        elif option == 'front':
            print(front(queue))
        elif option == 'back':
            print(back(queue))
        elif option == 'size':
            print(size(queue))
        elif option == 'empty':
            if size(queue) == 0:
                print(1)
            else:
                print(0)
        elif option == 'pop':
            print(pop(queue))