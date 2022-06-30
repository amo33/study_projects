import sys 
from collections import deque

stack = deque()

def push(val):
    stack.append(val)
def top():
    if size() !=0:
        return stack[-1]
    elif size() == 0:
        return -1
def size():
    return len(stack)

def pop():
    if size() != 0:
        return stack.pop()
    elif size() == 0:
        return -1

def empty():
    if size() == 0:
        return 1
    elif size() != 0:
        return 0

N = int(input())
for i in range(N):
    try:
        strinput = sys.stdin.readline().strip()
        func, val = strinput.split(' ')
    except:
        func = strinput.strip()
    finally:
        #print(func, val)
        if func == 'push':
            push(int(val))
        elif func == 'size':
            print(size())
        elif func == 'top':
            print(top())
        elif func == 'pop':
            print(pop())
        elif func == 'empty':
            print(empty())