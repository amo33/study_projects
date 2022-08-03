

def maxDepth(root) -> int:
    result = [0]
    def compareDepth(root,total):

        if root.left == None and root.right == None:
            print(root.val, total)
            result[0] = max(result[0], total)
            print(result)
        if root.left != None:
            compareDepth(root.left, total+1)
        if root.right != None:
            compareDepth(root.right,total+1)
    compareDepth(root,0)
    return result[0]
