import sys 
INF = 100000
# 간선은 모두 이차원 배열처럼 구성되어야합니다. 

weights = [
    [0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]
]
visited_weight = [INF for _ in range(6)]
visited = [0 for _ in range(6)]
def dij(val, start):
    visited[val] = 1
    for i in range(6):
        if val != i and val != start and i!= start:
            if visited_weight[val] + weights[val][i] < visited_weight[i]:
                visited_weight[i] = visited_weight[val] + weights[val][i] 
    
    