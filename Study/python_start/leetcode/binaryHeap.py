class BinaryHeap(object):
    def __init__(self) -> None:
        self.items = [None] # heap은 인덱스 1부터 시작 
    
    def __len__(self) -> int:
        return len(self.items) - 1
    
    def _prelocate_up(self):
        i = len(self.items)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]
                parent = i 
            else:
                break 
            parent = i //2 
        
    def insert(self, val):
        self.items.append(val) # insert it at the most left lead space 
    
    def _prelocate_down(self,idx):
        left = idx *2 
        right = idx * 2+1
        smallest = idx 

        if left<= len(self.items) and self.items[smallest] > self.items[left]:
            smallest = left 
        if right <= len(self.items) and self.items[smallest] > self.items[right]:
            smallest = right
        if smallest != idx:
            self.items[smallest], self.items[left] = self.items[left], self.items[smallest]
            self._prelocate_down(smallest)

    def extract(self) -> int:
        value , self.items[1] = self.items[1], self.items[-1]
        self.items.pop() # delete the last one since it is already at the top. 
        self._prelocate_down(1)

        return value 
        