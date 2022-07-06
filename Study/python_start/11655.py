import sys , string 

string_input = sys.stdin.readline().rstrip('\n') # \n 제거 
for i in range(len(string_input)):
    if string_input[i] in string.ascii_lowercase:
        print(chr((ord(string_input[i])-97+13)%26+97),end='')
    elif string_input[i] in string.ascii_uppercase:
        print(chr((ord(string_input[i])-65+13)%26+65),end='')
    elif string_input[i] in string.digits:
        print(string_input[i], end='')
    elif string_input[i] in string.whitespace:
        print(string_input[i], end='')