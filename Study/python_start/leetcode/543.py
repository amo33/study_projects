def diameterOfBinaryTree(root) -> int:
    result = [0]
    def dfs(val,total):
        if val.left == None and val.right == None:
            result[0] = max(result[0], total) 
            return 
        if val.left:
            dfs(val.left, total+1)
        if val.right:
            dfs(val.right, total+1)
    dfs(root.left,0)
    left , result[0]= result[0] , 0
    dfs(root.right,0)
    right = result[0]
    return left+right+2 