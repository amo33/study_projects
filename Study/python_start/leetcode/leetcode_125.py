import string , re , collections
# def isPalindrome(s: str) -> bool:
#     # regex = re.compile('[^0-9a-zA-Z]')
#     refined = re.sub('[^0-9a-zA-Z]', '', s)
#     print(refined)
#     refined = [refined[i].lower()  if 64<ord(refined[i]) <= 90 else refined[i] for i in range(len(refined))]
#     print(refined)
#     mid = len(refined) //2

#     end = len(refined) -1
#     start = 0 
#     for i in range(mid):
#         if refined[start+i] != refined[end-i]:
#             return False 
#     return True 
def isPalindrome(s: str) -> bool:
    string_check = collections.deque()
    for character in s:
        if character.isalnum():
            string_check.append(character.lower())
    while len(string_check) > 1:
        if string_check.popleft() != string_check.pop():
            return False 
    return True
string_input = input()
print(isPalindrome(string_input))