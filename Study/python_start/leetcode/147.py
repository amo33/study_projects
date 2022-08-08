class ListNode:
    def __init__(self,val= 0, next=None) -> None:
        self.val =  val 
        self.next = next 

def insertionSortList(head) :
        cur = parent =ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next 
            cur.next , head.next , head = head, cur.next, head.next 
            if head and cur and cur.val > head.val:
                cur = parent 
                # 만약 이 다음에 들어갈 값보다 현재 맨 끝값보다 작다면, 이 앞에 있다는 의미이기에 다시 처음부터 탐색하는 것
        return parent.next