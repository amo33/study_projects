class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
        root = TreeNode()
        
        def recurrent(tree1, tree2,root):
            if tree1 is None and tree2 is None:
                return 
            if tree1 is None:
                tree1 = TreeNode(0)
            if tree2 is None:
                tree2 = TreeNode(0)
            value = 0
            if tree1:
                value += tree1.val 
            if tree2:
                value += tree2.val
            
            root = TreeNode(value)
            # print(root, value)
            if tree1.left != None or tree2.left != None:
                root.left=recurrent(tree1.left, tree2.left, root.left)
            if tree1.right != None or tree2.right != None:
                root.right=recurrent(tree1.right, tree2.right, root.right)
            return root # recurrent 시 root를 return 해줘야한다.
        root =recurrent(root1, root2, root)
        return root