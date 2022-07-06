import string

tmp = string.digits+string.ascii_uppercase
# def convert(num, base) :
#     q, r = divmod(num, base)
#     if q == 0 :
#         return tmp[r] 
#     else :
#         return convert(q, base) + tmp[r]
N, M = input().split()
print(int(N,int(M)))
# print(convert(N,10))