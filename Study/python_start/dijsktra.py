import heapq , sys 
INF = 10000000
weights = [
    [0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]
]
heap = []
visited= [0 for _ in range(6)]
d = [INF for _ in range(6)]
d[0] = 0 
heapq.heappush(heap,(0,0))
def dij():
    while heap: #heapq를 이용함으로써 현재 가지고 있는 것중에서 제일 작은 값을 뽑아내는 것이다.
        dist, current_node=heapq.heappop(heap) 
        #print(dist, current_node)
        visited[current_node] = 1
        for i in range(6):
            if i != current_node and weights[current_node][i] != INF:
                #print(i, weights[current_node][i])
                if dist + weights[current_node][i] < d[i]:
                    d[i] = dist + weights[current_node][i]
                    print(*d)
                    heapq.heappush(heap, (d[i], i))
print(*d)
dij()
print(*d)