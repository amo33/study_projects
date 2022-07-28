import collections

class Listnode:
    def __init__(self,key=None,val=None ,next=None) -> None:
        self.val = val 
        self.key = key
        self.next = next 
    

class HashMap:
    
    def __init__(self) -> None:
        self.size = 1000 
        self.table = collections.defaultdict(Listnode)
    
    def put(self, key, val):
        index = key % self.size
        if self.table[index].val == None: #아예 없는 경우 
            self.table[index].val = val
            self.table[index].key = key  
            return 
        pointer = self.table[index]
        while pointer:
            if pointer.key == key: # key is one to one relation with value. The collision is occurred if at least 2 of inputs have the same hashkey! (Totally different!) 
                pointer.val = val 
                return 
            if pointer.next is None: # pointer 맨 끝에 새로운 값을 넣어줘야하기 때문이다.
                break 
            pointer = pointer.next 
        pointer.next = Listnode(key,val)
    
    def get(self, key):
        index = key % self.size 
        if self.table[index].val == None: 
            return -1 
        pointer = self.table[index]
        while pointer:
            if pointer.key == key:
                return pointer.val 
            pointer = pointer.next 
        return -1 
    
    def remove(self,key):
        index = key % self.size 
        if self.table[index].val == None:
            return 
        pointer = self.table[index]
        if pointer.key == key:
            self.table[index] = Listnode() if pointer.next == None else pointer.next
            return 
        pre = pointer 
        while pointer:
            if pointer.key == key:
                pre.next = pointer.next
                return
            pre , pointer = pointer, pointer.next 
        return -1 

    
            
                
