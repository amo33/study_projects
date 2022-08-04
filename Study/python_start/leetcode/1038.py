
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    sum_value : int = 0
    pre_val : int = 0
    val : int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        if root: # 더 빠른 방식 -- faster method 
            self.bstToGst(root.right)
            self.val += root.val 
            root.val = self.val 
            self.bstToGst(root.left)
        return root
#         def sumall(node):
#             if not node:
#                 return  
#             self.sum_value += node.val 
#             if node.left:
#                 sumall(node.left)
#             if node.right:
#                 sumall(node.right)
                
#         def inorder(root):
#             if root.left:
#                 inorder(root.left)
#             temp = root.val
#             root.val = self.sum_value - self.pre_val 
#             self.sum_value = root.val 
#             self.pre_val = temp 
#             if root.right:
#                 inorder(root.right)
        
#         sumall(root)
#         inorder(root)
#         return root