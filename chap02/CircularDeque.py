# 상속을 이용한 덱의 구현
from ArrayQueue import ArrayQueue

# 원형 덱: 큐를 상속한 클래스 정의
class CircularDeque(ArrayQueue):
    def __init__(self, capacity = 10):
        super().__init__(capacity)

    # 원형 덱: 동작이 동일한 연산
    def addRear(self, item):
        self.enqueue(item)
    
    def deleteFront(self):
        return self.dequeue()
    
    def getFront(self):
        return self.peek()
    
    # 원형 덱: 추가된 연산
    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            pass
    
    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else:
            pass

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            pass
