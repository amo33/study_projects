class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers( l1, l2):
    root =result_lst =ListNode(None)
    next = 0
    while l1 and l2:
        
        next , current = divmod(l1.val+l2.val +next,10)
        result_lst.next = ListNode(current)
        result_lst = result_lst.next 
       
        l1 = l1.next 
        l2 = l2.next 
    if l1:
        while l1:
            next , current = divmod(l1.val+ +next,10)
            result_lst.next = ListNode(current)
            result_lst = result_lst.next 
            l1 = l1.next
    elif l2:
        while l2:
            next , current = divmod(l1.val+l2.val +next,10)
            result_lst.next = ListNode(current)
            result_lst = result_lst.next 
            l2 = l2.next 
    if next ==1:
        result_lst.next = ListNode(next)
    return root.next