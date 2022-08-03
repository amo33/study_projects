import heapq, collections
def findCheapestPrice( n: int, flights, src: int, dst: int, k: int) -> int:
    map_list = collections.defaultdict(list)
   
    for source, dest , weight in flights:
        map_list[source].append([dest,weight])

    queue = [(0,src,0)]
    visited = [float('inf')]*(n+1)
    step_count = [float('inf')]*(n+1)

    while queue:
        cost, node ,status_step= heapq.heappop(queue)
        if node == dst: 
            return cost
        if status_step >=k+1:
            continue
        if status_step >= step_count[node]:
            continue
        step_count[node] = status_step
        
        for v,w in map_list[node]:
            alt = cost + w
            visited[v] = visited[node]-1
            heapq.heappush(queue,(alt,v,step_count[node]+1))
    return -1 
n = 4


flights =[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]

src = 0
dst = 3
k = 1
print(findCheapestPrice(n,flights, src, dst, k ))
13

10
1
10
# def findCheapestPrice( n: int, flights, src: int, dst: int, k: int) -> int:
#     map_list = collections.defaultdict(list)
#     for src, dest , weight in flights:
#         map_list[src].append([dest,weight])
#     visited = [float('inf') ]* (n+1)
#     def dfs(val,dst,k):
#         queue = []
#         heapq.heappush(queue, (0,val))
#         visited[val] = 0
#         while queue and k:
#             weight, node = heapq.heappop(queue)
#             while map_list[node]:
#                 value, w = map_list[node].pop(0)
#                 visited[value] = min(visited[value], visited[node]+w)
#                 print(visited)
#                 heapq.heappush(queue,(visited[value],value))
#             k-= 1
        
#         return visited[dst]
#     result= dfs(src, dst, k)
#     if result == float('inf'):
#         return -1
#     else:
#         return result 