class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        
        if len(inorder) == 0:
            return 
        # print(preorder,inorder)
        root_value = preorder.pop(0)
        root_index = inorder.index(root_value)
        root = TreeNode(root_value)
        # lefts = [val for val in preorder if val in set(inorder[:root_index])]
        # rights = [val for val in preorder if val in set(inorder[root_index+1:])]
        root.left = self.buildTree(preorder,inorder[:root_index])
        root.right = self.buildTree(preorder,inorder[root_index+1:])
        
        return root 