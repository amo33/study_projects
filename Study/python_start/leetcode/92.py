class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse(head, idx):
    root = result = ListNode(None)
    while idx >0:
        idx -=1 
        b = head 
        b.next, result.next = result.next , b         
        head = head.next 
    return root.next , head

def reverseBetween(head, left: int, right: int):
    left -=1 
    right -=1 
    root = result = ListNode(None)
    for _ in range(left):
        result.next = head 
        head = head.next 
        result = result.next 
    reverse_lst , next_lst = reverse(head,right-left)
    result.next = reverse_lst 
    while next_lst:
        reverse_lst.next = next_lst 
        next_lst = next_lst.next 
        reverse_lst = reverse_lst.next 
    
    return root 
