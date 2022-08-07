class TrieNode:
    def __init__(self) -> None:
        self.word = False 
        self.children = {} #defaultdict도 있지만, search 와 startwith keyerror를 위해 그냥 dictionary 쓰겠다.
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word:str) -> None:
        node = self.root 
        for char in word:
            if char not in node.children.keys():
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True # leaf node들은 모두 True
    
    def search(self, word:str) -> bool:
        node = self.root 
        for char in word:
            if char not in node.children.keys():
                return False 
            node = node.children[char]
        return node.word 
    def startswith(self, word:str) -> bool:
        node = self.root 
        for char in word:
            if char not in node.children.keys():
                return False 
            node = node.children[char]
        return True 