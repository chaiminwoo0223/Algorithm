# 단순 연결 구조를 위한 Node 클래스
class Node:
    def __init__(self, elem, link = None):
        self.data = elem # 데이터 멤버 생성 및 초기화
        self.link = link # 링크 생성 및 초기화

    # Node 클래스: append(Node) 연산
    def append(self, node):
        if node is not None:
            node.link = self.link
            self.link = node

    # Node 클래스: popNext() 연산
    def popNext(self):
        next = self.link
        if next is not None:
            self.link = next.link
        return next
    

# 단순 연결 리스트 클래스 정의와 생성자
class LinkedList:
    def __init__(self):
        self.head = None

    # LinkedList 연산: 포화, 공백 상태 검사
    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False
    
    # LinkedList 연산: getNode(pos)
    def getNode(self, pos):
        if pos < 0:
            return None
        ptr = self.head # 시작 위치: head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr
    
    # LinkedList 연산: getEntry(pos)
    def getEntry(self, pos):
        node = self.getNode(pos) # pos번째 노드를 구함
        if node == None:
            return None
        else:
            return node.data
        
    # LinkedList 연산: 삽입 연산 insert(pos, e)
    def insert(self, pos, e):
        node = Node(e, None)
        before = self.getNode(pos-1)
        if before == None: # before가 None이면 멘 앞에 추가하고, 리스트의 머리노드(head)가 변경됨
            node.link = self.head
            self.head = node
        else:
            before.append(node)

    # LinkedList 연산: 삭제 연산 delete(pos)
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.link
            return before
        else:
            return before.popNext()
        
    # LinkedList 연산: 전체 요소의 수 size()
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None: # 머리노드부터 링크를 따라 None이 될 때까지 이동하면서, 이동 횟수를 기록함
            ptr = ptr.link
            count += 1
        return count
    
    # LinkedList 연산: 화면 출력 display()
    def display(self, msg = 'LinkedList:'):
        print(msg, end='')
        ptr = self.head
        while ptr is not None: # 머리노드부터 링크를 따라 None이 될 때까지 이동하면서, 현재 노드의 데이터를 화면에 출력함
            print(ptr.data, end=' -> ')
            ptr = ptr.link
        print("None")

    # LinkedList 연산: 교체 연산 display(pos, e) --> 추가
    def replace(self, pos, e):
        node = self.getNode(pos)
        if node is not None:
            node.data = e
