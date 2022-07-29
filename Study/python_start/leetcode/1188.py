from threading import Semaphore, Lock 

# MultiThreading example code using Semaphore and Lock 
class BoundedBlockingQueue(object):

    def __init__(self, capacity : int ) -> None:
        self.c = capacity # 저장가능한 용량
        # lock과 semaphore는 접근을 제한하는 방식 
        # 여러개의 thread가 동시에 접근할때, 접근하는 순서에 따라서 결과가 random하게 되는 것을 막는 방식이다.
        self.pulling = Semaphore(0) # 처음에는 아무것도 없기 때문에 0으로 선언해야 아직 가질 수 있는 값이 없습니다. 
        self.pushing = Semaphore(self.c) # pushing이란 semaphore는 c만큼 갖고 있다.# 0 = acquire가 blocked / 1이면 acquire ok
        self.editing = Lock()  # unlock == acquire한 상태 / lock == acquire X 
        self.data = [] # data 저장할 array 

    
    def enqueue(self, element: int) -> None:
        self.pushing.acquire() # 3 => 2 
        self.editing.acquire() # unlock => lock , 현재 작업을 진행할것이므로 acquire로 진행 
        self.data.append(element) # 값 append 
        self.editing.release() # 이제 다 작업한 상태이므로 끝 
        self.pulling.release() # 0 => 1 로 증가. 0에서 1로 되면 dequeue가 될 element가 있다. 
    
    def dequeue(self) -> int:
        self.pulling.acquire() # 0 == blocking / 1== acquire() 값이 있으면 acquire 
        self.editing.acquire() # dequeue를 진행할 것이기에 lock도 acquire 
        item = self.data.pop(0) # dequeue 
        self.editing.release() # dequeue 진행했으니 다시 lock 원상 복귀 
        self.pushing.release() # pushing에도 +1 , 하나를 추출했으니 공간이 하나 생겼다.
        return item 
    
    def size(self) -> int:
        return len(self.data)