import heapq

# using priority queue, we are going to insert with given index. 
# - greedy method is acceptable since we are assigning with tallest person
def reconstructQueue(people):
        heap = []
        
        for person in people:
            heapq.heappush(heap, [-person[0],person[1]])
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0],person[1]]) # O(n) 시간이 걸린다.
        return result 