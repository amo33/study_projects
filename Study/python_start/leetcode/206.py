class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def reverselist(head):
    def reverse(node, pre):
        if not node:
            return pre 
        next , node.next = node.next , pre 
        return reverse(next, node)
        
    return reverse(head)