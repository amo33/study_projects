import collections

def groupAnagrams(strs):
    anagram_set = {}
    for str_in in strs:
        # print(str_in)
        sorted_str = ''.join(sorted(list(str_in)))
        # print(sorted_str)
        if sorted_str in list(anagram_set.keys()):
            anagram_set[sorted_str].append(str_in)
        else:
            anagram_set[sorted_str] = []
            anagram_set[sorted_str].append(str_in)
    return list(anagram_set.values())

strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["a"]
print(groupAnagrams(strs))