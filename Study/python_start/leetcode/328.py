class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def oddEvenList(head):

    root = result = ListNode(None)
    even_lst = ListNode(None)
    result.next = head 
    while head:
        b = head.next
        head.next = b.next 
        b.next = head 
        
        result.next = b
        even_lst.next = b.next 

        head = head.next 
        result = result.next 
        even_lst = even_lst.next 
    if head:
        result.next = head 
        result = result.next 
        even_lst.next = None  
    result.next = even_lst.next 
    return root.next     
    
        