class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head ):
        def reverse(node, pre=None):
            if not node:
                return pre
            next, node.next = node.next , pre 
            return reverse(next, node)
        return reverse(head)
            