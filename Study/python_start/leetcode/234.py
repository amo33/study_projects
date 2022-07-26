class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def _add(self, x):
        self.next = ListNode(x)
    def last(self):
        print(self.val)

def palidromelinked(lists):
    result_lst = []
    result_lst[lists.val]
    while lists.next:
        lists = lists.next
        result_lst.append(lists.val)
    return result_lst == result_lst[::-1]