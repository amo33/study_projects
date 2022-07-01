from __future__ import print_function
import sys 

# text = 'ababacabacaabacaaba'
# str_example = 'abacaaba'
text = sys.stdin.readline()[:-1]
str_example = sys.stdin.readline()[:-1]
# print(text)
# print(str_example)
lst = [0 for _ in range(len(str_example))]
def find_pre_sub(val_string):
    i = 1
    j = 0
    if i == len(val_string): # 길이가 1인걸 예외처리했습니다.
        if val_string[j] == val_string[i-1]:
            j+=1
            lst[i-1] = j
            i+=1
    while i < len(val_string):
        # print(i, lst)
        if val_string[j] == val_string[i]:
            j +=1
            lst[i] = j 
            i +=1
        else:
            if j != 0:
                j = lst[j-1]
            else:
                i +=1
    
find_pre_sub(str_example)
# print(lst)

def kmp(text, pattern):
    cnt = 0
    result_lst = []
    i = 0
    j = 0
    if i == len(text)-1: # 길이가 1인 경우를 예외처리했습니다.
        if pattern[j] == text[i-1]:
            result_lst.append(i-j+1)
            j+=1
            i+=1
            cnt+=1
    while i < len(pattern):
        # print(j,i)
        if text[j] == pattern[i]:
            if j == len(text)-1:
                result_lst.append(i-j+1)
                # print("matched",j,i)
                cnt += 1
                
                j = lst[j-1]
                # print(j,i)
            else:
                i+=1
                j+=1 
        elif text[j] != pattern[i]: 
            # print("not matching")
            # time.sleep(1)
            if j != 0:
                j = lst[j-1]
            else:
                i+=1
            #print(j, i)
    return cnt ,result_lst
cnt, total = kmp(str_example, text)
print(cnt)
for i in range(cnt):
    print(total[i], end=' ')
print()

