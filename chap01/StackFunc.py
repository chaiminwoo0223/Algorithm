# 스택을 위한 데이터
capacity = 10
array = [None]*capacity
top = -1 # 상단의 인덱스: 공백 상태(-1)로 초기화

# 스택의 공백 상태와 포화 상태 검사
def isEmpty():
    return top == -1
    
def isFull():
    return top == capacity-1

# 스택의 삽입 연산
def push(e):
    if not isFull():
        top += 1
        array[top] = e
    else:
        print("stack overflow")
        exit()

# 스택의 삭제 연산
def pop():
    if not isEmpty():
        top -= 1
        return array[top+1]
    else:
        print("stack underflow")
        exit()

# 스택의 peek() 연산
def peek():
    if not isEmpty():
        return array[top]
    else:
        pass

# 스택의 size() 연산
def size():
    return top+1
