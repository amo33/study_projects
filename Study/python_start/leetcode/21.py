class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def mergetwolist(list1, list2):
    root =result_lst =ListNode(None)
    while list1 and list2:
        if list1.val <= list2.val:
            result_lst.next = ListNode(list1.val)
            list1 = list1.next 
            
        elif list2.val < list1.val:
            result_lst.next = ListNode(list2.val)
            list2 = list2.next 
        result_lst = result_lst.next
    if list1:
        while list1:
            result_lst.next = ListNode(list1.val)
            list1 = list1.next 
            result_lst = result_lst.next
    elif list2:
        while list2:
            result_lst.next = ListNode(list2.val)
            list2 = list2.next 
            result_lst = result_lst.next
    return root.next
