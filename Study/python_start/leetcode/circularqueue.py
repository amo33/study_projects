class circularqueue:

    def __init__(self, k : int ) -> None:
        self.q = [None] * k 
        self.maxlen = k 
        self.p1 = 0 
        self.p2 = 0 
    def enQueue(self ,x ):
        if self.q[self.p2] is None:
            self.q[self.p2] = x 
            self.p2  = (self.p2 +1) % self.maxlen
            print(self.p2)
            return True 
        else:
            return False 
    def deQueue(self):
        if self.q[self.p1] != None:
            self.q[self.p1] = None 
            self.p1 = (self.p1 +1) % self.maxlen
            return True 
        elif self.q[self.p1] == None:
            return False 
    def Front(self) -> int:
        return -1 if self.q[self.p1] == None else self.q[self.p1]
    
    def Rear(self) -> int:
        return -1 if self.q[self.p2] == None else self.q[self.p2]

    def isEmpty(self) -> int:
        return self.p1 == self.p2 and self.q[self.p1] == None 
    def isFull(self) -> int:
        return self.p1 == self.p2 and self.q[self.p1] != None 
obj = circularqueue(3)
param_11 = obj.enQueue(1)
param_12 = obj.enQueue(2)
param_13 = obj.enQueue(3)
print(obj.Rear())
print(obj.Front())
param_14 = obj.enQueue(4)
param_2 = obj.deQueue()
param_3 = obj.Front()

param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()
