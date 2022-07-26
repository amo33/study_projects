class Node:
    def __init__(self, value, right_node=None, left_node=None):
        self.value = value
        self.left = right_node  # doubly linked list
        self.right = left_node  


class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = Node(None), Node(None)   
        self.maxlen = k                              
        self.len = 0                               
        self.head.right = self.tail                     
        self.tail.left  = self.head                     

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            new_node = Node(value)  # 삽입할 노드 생성
            head_next = self.head.right  # head 다음의 노드를 따로 저장 (본래 head <-> head_next)
            self.head.right, head_next.left = new_node, new_node  # head->new_node & new_node <- head_next
            new_node.left, new_node.right = self.head, head_next  # head<-new_node & new_node -> head_next
            self.len += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
           new_node = Node(value)
           tail_left = self.tail.left 
           self.tail.left, tail_left.right = new_node, new_node 
           new_node.left , new_node.right = tail_left, self.tail 
           self.len +=1
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            head_right = self.head.right.right  # head <-> head.right <-> head.right.right
            head_right.left, self.head.right = self.head, head_right # head <-> head.right.right
            self.cur_size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            tail_before = self.tail.left.left  # tail.left.left <-> tail.left <-> tail
            tail_before.right, self.tail.left = self.tail, tail_before  # tail.left.left <-> tail
            self.cur_size -= 1
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.head.right.value  # head <-> head.right

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.tail.left.value  # tail.left <-> tail

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cur_size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cur_size == self.max_size