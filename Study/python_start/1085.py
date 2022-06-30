import sys 
import math 
input = sys.stdin.readline

x,y,w,h = map(int, input().split(' '))
width = abs(x) if abs(x-w) > abs(x) else abs(x-w) 
height = abs(y) if abs(y-h) > abs(y) else abs(y-h)
if width > height:
    print(height)
else:
    print(width)

