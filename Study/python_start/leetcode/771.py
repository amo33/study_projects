import collections
def numJewelsInStones1(jewels: str, stones: str) -> int:
    jewels_lst = set(jewels)
    result = 0
    print(jewels_lst)
    for stone in stones:
        if stone in jewels_lst:
            result +=1 
    return result

jewels = 'aA'
stones = "aAAbbbb"
print(numJewelsInStones1(jewels,stones))

def numJewelsInStones2(jewels: str, stones: str) -> int: # defaultdict 사용 
    freq = collections.defaultdict(int) # int형 초기화  
    for stone in stones:
        freq[stone] +=1 
    result = 0
    for s in jewels:
        result += freq[s] # jewel 중 freq에서 count됬던 값들을 더해준다. 
    return result 

def numJewelsInStones3(jewels: str, stones: str) -> int: # counter 사용 
    freq = collections.Counter(stones)
    result = 0
    for s in jewels:
        if s in freq.keys(): # defaultdict과 counter 모두 keyerror의 문제가 없어서 사용하기 용이하다.
            result += freq[s]
    return result