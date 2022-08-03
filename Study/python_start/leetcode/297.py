import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = collections.deque()
        nodequeue = collections.deque()
        nodequeue.append(root)
        def levelorder(root):
            
            while nodequeue:
                node = nodequeue.popleft()
                if node:
                    result.append(str(node.val))
                else:
                    result.append('null')
                    continue
                nodequeue.append(node.left)
                nodequeue.append(node.right)
        levelorder(root)

        
        
        result_str = ','.join(list(result)) # string으로 변환 
        print(result_str) # 중간 점검 
        return result_str # return string 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        data = ["F"] + data # 트리의 인덱스를 위해서 1번째 index부터 접근하게 했습니다.
        idx = 1
        # print(data)
        if data[1] == 'null' or data[1] == '':
            return None 
        root = TreeNode(None)
        def buildTree(data,root,idx):
            
            if len(data) <= idx:
                return 
            root = TreeNode(data[idx])
            if 2*idx < len(data):
                root.left = buildTree(data, root.left,2*idx)
            if 2*idx < len(data):
                root.right = buildTree(data, root.right, 2*idx+1)
            return root 
                
        root = buildTree(data,root,idx)    
        return root 