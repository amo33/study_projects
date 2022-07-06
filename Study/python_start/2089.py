import sys 
val =int(input())
val =abs(val)
#standard = '1'*(len(bin(val))-2) 
positvie = bin(val)[2:]
#print(standard)
print(bin(~(val+1)))