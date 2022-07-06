import sys 

input_string = sys.stdin.readline().strip()
i = 0
result_lst = [0 for _ in range(26)]
while i < len(input_string):

    #print(ord(input_string[i])-97)
    result_lst[ord(input_string[i])-97] +=1 
    i +=1
print(result_lst)
