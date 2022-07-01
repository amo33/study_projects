import sys 

str_val = 'abacaaba'
j = 0 
i = 1
lst = [0 for _ in range(len(str_val))] 
while i < len(str_val):
    print(j,i)
    if str_val[j] == str_val[i]:
        lst[i] = j+1
        print(j,i,lst)
        j+=1 
        i+=1 
    else:
        if j == 0: # j가 0인 경우는 i를 증가시키고, 나머지는 j를 뒤로 빼서 체크한다.
            i +=1 
        if j != 0:
            j = lst[j-1]
print(lst)
print(str_val,'ababacabacaabacaaba')
def count_string( lst,keystring ,str_val):
    i = 0  # index for txt[]
    j = 0  # index for pat[]
    while i < len(str_val):
        print(j,i)
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if keystring[j] == str_val[i]:
            i += 1
            j += 1
        # Pattern을 찾지 못한 경우
        elif keystring[j] != str_val[i]:
            # j!=0인 경우는 짧은 lps에 대해 재검사
            if j != 0:
                j = lst[j-1]
                print(j, keystring[j], str_val[i])
            # j==0이면 일치하는 부분이 없으므로 인덱스 증가
            else:
                i += 1

        # Pattern을 찾은 경우
        if j == len(keystring):
            print("Found pattern at index " + str(i-j))
            # 이전 인덱스의 lps값을 참조하여 계속 검색
            j = lst[j-1]
print(count_string(lst,str_val,'ababacabacaabacaaba'))