import sys 
import string 
A, B = sys.stdin.readline().split()
M = int(input())
arr = list(map(int,sys.stdin.readline().strip().split()))
# print(arr)
# bit_string = int(''.join(arr))
total_lst = string.digits + string.ascii_uppercase
arr_convert = list(map(lambda x: total_lst[x], arr))
bit_string = ''.join(arr_convert)

tmp =[str(i) for i in range(int(B))] 
# print(bit_string)
ten_String = int(bit_string, int(A))
# print(ten_String)
def convert(num,base):
    q, r = divmod(num,base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q,base) + ','+ tmp[r]
for string_val in convert(ten_String, int(B)):
    if string_val != ',':
        print(string_val, end='')
    else:
        print(end=' ')
