
def longestPalindrome( s):
    result = ''
    def expand(s, left, right):
        while 0<=left and right < len(s) and s[left] == s[right]:
            left -=1 
            right +=1
        return s[left+1:right]

    if len(s)<2 and s[:] == s[::-1]:
        return s 
    for i in range(len(s)-1):
        result = max(result, expand(s,i,i+1),expand(s,i,i+2),key=len)
    return result 

s = "cbbd"
print(longestPalindrome(s))
        