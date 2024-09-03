# chap02: ArrayQueue 클래스(큐)
class ArrayQueue:
    # 원형 큐: 생성자
    def __init__(self, capacity = 10):
        self.capacity = capacity # 용량(고정)
        self.array = [None]*capacity # 요소들을 저장할 배열
        self.front = 0 # 전단 인덱스
        self.rear = 0 # 후단 인덱스

    # 원형 큐: 공백 상태 검사
    def isEmpty(self):
        return self.front == self.rear
    
    # 원형 큐: 포화 상태 검사
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    # 원형 큐: 삽입 연산
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            pass

    # 원형 큐: 삭제 연산
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            pass
        
    # 원형 큐: 상단 들여다보기 연산
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity] 
        else:
            pass
    
    # 원형 큐: 전체의 수
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    # 원형 큐: 전체 요소를 화면으로 출력
    def display(self, msg):
        print(msg, end=' = [ ')
        for i in range(self.front+1, self.front+1+self.size()):
            print(self.array[i % self.capacity], end=' ')
        print(']')

    # 원형 큐: 링 버퍼를 위한 삽입 연산
    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty(): # rear == front
            self.front = (self.front + 1) % self.capacity