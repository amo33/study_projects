import heapq

heap= []
lists = [[1,4,5],[1,3,4],[2,6]]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def _add(self, x):
        self.next = ListNode(x)
    def last(self):
        print(self.val)
def mergeKLists(lists):
    root =result = ListNode(None)
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next 
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
        
    return root.next