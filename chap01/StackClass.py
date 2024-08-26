# 스택 클래스 정의
class ArrayStack:
    # 스택의 생성자
    def __init__(self, capacity):
        self.capacity = capacity # 스택 용량
        self.array = [None]*capacity # 요소 배열
        self.top = -1 # 상단의 인덱스
    
    # 스택 클래스의 연산
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity-1
    
    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else:
            pass

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass

    def size(self):
        return self.top+1
