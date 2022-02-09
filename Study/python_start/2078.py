import sys

left = 0
right = 0

input = sys.stdin.readline

a , b = map(int, input().split())

while ((a != 1) or (b != 1)):

    if a == 1:
        b -= 1
        right += 1
    elif b == 1:
        a -= 1
        left += 1
    elif a < b:
        b -=a
        right += 1
    elif a > b:
        a -= b
        left += 1
    else:
        break
    
    
print(left,right)