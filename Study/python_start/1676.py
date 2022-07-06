def factorial(val):
    if val == 0:
        return 1
    return factorial(val-1) * val 
val = factorial(int(input()))
cnt = 0
while True:
    if val % 10**(cnt+1) == 0:
        cnt +=1 
    else:
        break # for consecutive search 
print(cnt)