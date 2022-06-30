import sys 

input = sys.stdin.readline

test = int(input())

for i in range(test):
    H,W,N = map(int, input().split()) 
    width = 0
    if (N%H != 0 and N/H != 0): # 6 12 7 
        width = int(N / H) + 1  # 
    elif (N%H != 0 and N /H ==0): # 6 12 5 
        width = 1
    else:
        width = int(N/H) # 1 20 20 
    height = H if N % H ==0 else N % H # 이건 따로 
    if width < 10 : 
        print(str(height) + '0' +str(width))
    else:
        print(str(height)+str(width))