import heapq
def kClosest(points, k: int): 
    # heapq를 사용한것이 sorted 방식보다 더 좋다. sorted 는 key로 정렬했는데 그게 더 큰 시간이 걸린다. 
    # 아무래도 sorted 방법과 다르게 heapq는 k만 나오면 끝나기 때문이고, sorted는 전체 리스트를 다루기에 시간이 더 걸린다.
        heap =[]
        for (x,y) in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist,x,y))
        
        result = []
        for _ in range(k):
            dist , x, y = heapq.heappop(heap)
            result.append([x,y])
        return result