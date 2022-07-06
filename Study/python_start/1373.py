# import sys 
# bin_num = sys.stdin.readline()
# ten_num = int(bin_num, 2)
# print(oct(ten_num)[2:])

import sys 
oct_num = sys.stdin.readline()
ten_num = int(oct_num, 8)
print(bin(ten_num)[2:])