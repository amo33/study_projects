import sys 

input = sys.stdin.readline

count = int(input())

for i in range(count):
    case = input()
    consecutive = 0
    result = 0
    for target in case:
        if target == 'O':
            consecutive+= 1
            result += consecutive
        elif target =='X':
            consecutive = 0
            result += consecutive
    print(result)