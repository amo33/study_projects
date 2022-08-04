import collections 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    value : int = 0
    dist : int = 10**5
    def minDiffInBST(self, root) -> int:
        result = 10**5
        status = collections.deque()
        def check(root,flag):
            if root.left:
                check(root.left,0)
            if flag != 1:
                self.dist = min(self.dist, abs(self.value - root.val))
            if root.right:
                check(root.right,0)
        status.append(root)
        while status:
            node = status.popleft()
            self.value = node.val 
            self.dist = 10**5
            check(node,1)
            if node.left:
                status.append(node.left)
            if node.right:
                status.append(node.right)
            result = min(result, self.dist)
        return result