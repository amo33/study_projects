class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    root = result = ListNode(None)
    result.next = head
    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head 
        
        result.next = b 
        
        result = result.next.next 
        head = head.next
        
    
    return root.next 
        

    