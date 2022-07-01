import sys 
from collections import deque 
paranthesis = sys.stdin.readline()
def extract_stick(str_val):
    # print(len(str_val))
    stack = deque()
    # stack.append(str_val[0])
    # # j = 1 
    # #stick_given = {}
    given_stick = 0
    total_stick = 0
    for j in range(len(str_val)):
        if str_val[j] == ')':
            try:
                stack.pop()
            except:
                pass 
            if str_val[j-1] != '(':
                given_stick -= 1 # 초기화 
                total_stick +=1
        if str_val[j] == '(':
            stack.append(str_val[j])
            if str_val[j+1] != ')':
                given_stick +=1
                # print(j, given_stick)
            if str_val[j+1] == ')':
                # print("sum",j, total_stick, given_stick)
                total_stick += given_stick 
            j+=1
    return total_stick
print(extract_stick(paranthesis))