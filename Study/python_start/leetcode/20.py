import collections
# stack1 = 0
# stack2 = 0
# stack3 = 0
# s = "(]"
# for string_val in s:
#     if string_val == '(':
#         stack1+=1
#     elif string_val == ')':
#         stack1-=1
#     elif string_val == '{':
#         stack3 +=1
#     elif string_val == '}':
#         stack3 -= 1
#     elif string_val == '[':
#         stack2 +=1 
#     elif string_val == ']':
#         stack2 -=1
#     if stack1 < 0 or stack2 < 0 or stack3 < 0:
#         print(False)
# if stack1 == 0 and stack2 ==0 and stack3 == 0:
#     print(True) 
# else:
#     print(False) 
# def check_string(s):
#     for i in range(len(s)-1):
#         if s[i] == '(' and s[i+1] != ')':
#             return False
#         elif s[i] == '{' and s[i+1] != '}':
#             return False

#         elif s[i] == '[' and s[i+1] != ']':
#             return False
#         return True 
stack1 = collections.deque()
# stack2 = collections.deque()
# stack3 = collections.deque()
def check_string(s):
    if len(s) % 2 !=0:
        return False
    for i in range(len(s)):
        try:
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack1.append(s[i])
            else:
                if s[i] == ')':
                    if stack1.pop() != '(':
                        return False 
                elif s[i] ==']':
                    if stack1.pop() != '[':
                        return False 
                elif s[i] == '}':
                    if stack1.pop() != '{':
                        return False
            # elif s[i] == '[':
            #     stack2.append(i)
            # elif( s[i-1] != '{' and s[i-1] != '(') and s[i] == ']':
            #     stack2.pop()
            # elif s[i] == '{':
            #     stack3.append(i)
            # elif ( s[i-1] != '[' and s[i-1] != '(') and s[i] == '}':
            #     stack3.pop()
        except:
            return False
    if len(stack1) ==0:
        return True 
    else:
        return False
print(check_string("()"))
# stack1 = 0
# stack2 = 0
# stack3 = 0
# def check_string(s):
#     if len(s) % 2 != 0:
#             return False
#     for i in range(len(s)-1):
    
#         if s[i] == '(':
#             stack1 +=1
#             if (s[i+1] == '}' or s[i+1] == ']'):
#                 return False
#         elif s[i] == '{': 
#             stack2 +=1
#             if(s[i+1] == ']' or s[i+1] == ')'):
#                 return False

#         elif s[i] == '[':
#             stack3 +=1
#             if (s[i+1] == ')' or s[i+1] == '}'):
#                 return False
#     return True 