val = int(input())
mid = int((2*val -1)/2)
for i in range(val):
    if i == val-1:
        for j in range(2*val -1):
            print('*',end='')
    else:
        for j in range(mid+i+1):
            if j == mid - i or j == mid + i:
                print('*',end='')
            else:
                print(' ',end='')
    print()
