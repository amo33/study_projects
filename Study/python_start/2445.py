val = int(input())

for i in range(val*2):
    if i < val:
        for j in range(i+1):
            print('*',end='')
        for j in range(i+1, val):
            print(' ',end='')
        for j in range(i+1, val):
            print(' ',end='')
        for j in range(i+1):
            print('*',end='')
    elif i >= val:
        for j in range(2*val-i-1):
            print('*',end='')
        for j in range(i-val+1):
            print(' ',end='')
        for j in range(i-val+1):
            print(' ',end='')
        for j in range(2*val-i-1):
            print('*',end='')
    print()
    
    