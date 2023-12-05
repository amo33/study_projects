# LRU 알고리즘
'''
캐시 교체 알고리즘 중 하나 -> Least Recently Used의 약자다.
새로운 데이터가 발생했을 때, 가장 오래전에 사용된 데이터를 제거하고 새로운 데이터를 삽입하는 알고리즘

1. 새로운 데이터가 들어온 경우 : cache miss
    1-1. cache에 넣어준다.
    1-2. cache가 가득 찼다면, 가장 오래된 데이터를 제거하고 넣어준다.
2. 존재하는 데이터가 들어온 경우 : cache hit 
    2-1. 해당 데이터를 꺼낸 후
    2-2. 가장 최근 데이터 위치로 보낸다.

1.  size < cache size 일때
    있는지 확인
     있으면 -> 시간 +1 , e 제거 후 다시 add
     없으면 -> 시간 +5, 그냥 add
2. size == cache size 일때
    있는지 확인
     있으면 -> 시간 +1 , e 제거후 다시 add
     없으면 -> 시간 +5 , set의 가장 앞의 요소를 제거 후 e를 add
'''
import sys
N = int(input())
if N == 0:
    print("No cache is used!")

def static_cache(cache_size):
    def real_decorator(func):
        cache = []
        def wrap(*args,**kwargs):
            nonlocal cache  # 여기서 'cache'를 nonlocal로 선언
            exec_time = 0
            for city in args[0]:  # 'args[0]'는 'cities' 리스트
                city = city.lower()
                if city in cache:
                    cache.remove(city)
                    cache.append(city)
                    exec_time +=1
                else:
                    if len(cache) == cache_size:
                        cache.pop(0)
                    cache.append(city)
                    exec_time += 5
            return exec_time
        return wrap
    return real_decorator

@static_cache(cache_size=N)
def solution(cities):
    pass  # 실제 로직은 데코레이터에 구현되어 있음

try:
    while True:
        current_input = sys.stdin.readline().strip().split()
        if not current_input: break
        print(solution(current_input))
except KeyboardInterrupt:
    print('Ctrl + C 중지 메시지 출력')
