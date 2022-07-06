import sys 
import string 
# strings = sys.stdin.readlines()
# string_array = [lines.rstrip() for lines in strings]
i = -1
while True:
    if i != -1:
        print()
    elif i == -1:
        i+=1 
    try:
        string_array = sys.stdin.readline().rstrip('\n')
        if(len(string_array)== 0):
            break
        lower, upper , number , space = 0 , 0, 0, 0
        for j in range(len(string_array)):
            if string_array[j] in string.ascii_lowercase:
                lower += 1 
            elif string_array[j] in string.ascii_uppercase:
                upper += 1
            elif string_array[j] in string.digits:
                number += 1
            elif string_array[j] in string.whitespace:
                space += 1
        print(lower,upper,number,space,end=" ")
    except:
        break
