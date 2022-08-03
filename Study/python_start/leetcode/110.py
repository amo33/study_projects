class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    shortest : int = 10**4
    longest : int = 0
    def isBalanced(self, root) -> bool:
        
        def check(node):
            if not node:
                return 0
            left = check(node.left) # left의 leaf 개수 반환 
            right = check(node.right) # '' '' ''
            
            if left == -1 or right == -1 or abs(left-right )> 1: # 만약 left or right 가 -1이거나 둘의 차이가 1 초과면 -1 
                return -1 
            return max(left,right)+1
        if check(root) == -1:
            return False 
        return True 