import sys 
N = int(input())
queue = list()

def push_back(x, queue):
    #new_lst = list(x)
    queue.append(x)
    # print(queue)
    return queue

def push_front(x, queue):
    new_lst = list()
    new_lst.append(x)
    new_lst.extend(queue)
    # print(new_lst.extend(queue))
    return new_lst

def size(queue):
    return len(queue)

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
def empty(queue):
    if size(queue) != 0:
        return 0
    else:
        return 1
def pop_front(queue):
    if size(queue) != 0:
        val = queue[0]
        del queue[0]
        return val , queue 
    else:
        return -1 , queue 
def pop_back(queue):
    if size(queue) != 0:
        val = queue[-1]
        del queue[-1]
        return val , queue 
    else:
        return -1 , queue 
for i in range(N):
    try:
        option_string = sys.stdin.readline().strip().split(' ')
        value = int(option_string[1])
        option = option_string[0]
        # print(option, value )
    except:
        option = option_string[0]
    
    finally:
        if option == 'push_back':
            queue = push_back(value, queue)
            # print(queue)
        elif option == 'push_front':
            queue = push_front(value, queue)
            # print(queue)
        elif option == 'front':
            print(front(queue))
        elif option == 'back':
            print(back(queue))
        elif option == 'size':
            print(size(queue))
        elif option == 'empty':
            print(empty(queue))
        elif option == 'pop_front':
            val , queue = pop_front(queue)
            print(val)
        elif option == 'pop_back':
            val, queue = pop_back(queue)
            print(val)
