import sys , math
val =int(input())
def extract_val(val):
    result_lst = ""
    if not val:
        return ("0")
    
    while val:
        if val % (-2):
            result_lst = "1"+result_lst
            print(val//-2, val - -2*(val//-2))
            val = val//-2 +1
        else:
            result_lst = "0" + result_lst
            val //= -2
    print(result_lst)
    return result_lst
result = extract_val(val)
print(result)
# converted = bin(2**(len(result)+1)-1)
# for i in range(len(result)):
#     if i % 2 == 1 and result[i] != 0:
#         tmp = 2**i 
#         converted_val = bin(int(converted & bin(tmp),2)+1)
#     elif i %2 == 0 and result[i] != 0:
#         converted = converted | bin(2**i)
# print(converted[2:])