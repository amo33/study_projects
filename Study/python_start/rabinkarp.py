import sys 
from functools import reduce
def get_hash(string_value):
    result = 0
    for i in range(len(string_value)):
        print(string_value[i], len(string_value) - 1- i)
        result += ord(string_value[i]) * 2**(len(string_value)-1 -i)
    return result 
def compare_string(pattern, text):
    for p in zip(pattern, text):
        if p[0] != p[1]:
            return False 
    return True
def check_string(pattern, text):
    pattern_hash = get_hash(pattern)
    pattern_length = len(pattern)
    text_hash = get_hash(text[:len(pattern)])
    print(pattern_hash, text_hash)
    print(len(pattern), len(text[:pattern_length]))
    j = 0
    print(pattern_length, len(text))
    while j <= (len(text) - pattern_length):
        print(pattern_hash, text_hash)
        if pattern_hash == text_hash:
            print(j +1, "index")
            if compare_string(pattern, text[j:j+pattern_length]) == True:
                print("true")
            else:
                print("false")
        # print(text[j+pattern_length], pattern_length-1, j)
        # print(ord(text[j])* 2**(pattern_length-1))
        try:
            text_hash = 2*(text_hash - ord(text[j])* 2**(pattern_length-1)) + ord(text[j+pattern_length])
        except:
            break
        j += 1
        
text = sys.stdin.readline()[:-1]
pattern = sys.stdin.readline()[:-1]
check_string(pattern, text)