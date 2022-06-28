import sys 

pattern_lst = []
def find_pattern(line):
    temp = True 
    pattern = []
    for i in line:
        if i == '(' or i == '[':
            pattern.append(i)
        elif i == ')':
            if not pattern or pattern[-1] == '[':
                temp = False
                break
            elif pattern[-1] == '(':
                pattern.pop()
        elif i == ']':
            if not pattern or pattern[-1] == '(':
              
                temp = False 
                break 
            elif pattern[-1] == '[':
                pattern.pop()
    if temp == True and not pattern:
        return True 
    else:
        return False
    
while True:
    lines = input()
    if lines != '.':
        if find_pattern(lines) == False:
            print('no')
        elif find_pattern(lines) == True:
            print("yes")
    else:
        break
    #readline은 input.stdin.readline인데, 하나만(한 줄만) 입력받는데 쓰면 \n도 같이 입력받기 때문에 여러줄을 받을때만 사용하는 것이 좋다.