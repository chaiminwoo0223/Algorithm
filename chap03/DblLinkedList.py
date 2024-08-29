# 이중 연결 구조를 위한 DNode 클래스 정의
class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem # 노드의 데이터 필드(요소)
        self.next = next # 다음 노드를 위한 링크
        self.prev = prev # 이전 노드를 위한 링크(추가됨)

    # DNode의 append(node) 연산
    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next = node

    # DNode의 popNext() 연산
    def popNext(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node
    
# 이중 연결 리스트 클래스 정의와 생성자
class DblLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False
    
    def getNode(self, pos):
        if pos < 0:
            return None
        ptr = self.head # 시작 위치: head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.next
        return ptr
    
    def getEntry(self, pos):
        node = self.getNode(pos) # pos번째 노드를 구함
        if node == None:
            return None
        else:
            return node.data
        
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None: # 머리노드부터 링크를 따라 None이 될 때까지 이동하면서, 이동 횟수를 기록함
            ptr = ptr.next
            count += 1
        return count
    
    def display(self, msg = 'DblLinkedList:'):
        print(msg, end='')
        ptr = self.head
        while ptr is not None: # 머리노드부터 링크를 따라 None이 될 때까지 이동하면서, 현재 노드의 데이터를 화면에 출력함
            print(ptr.data, end=' <=> ')
            ptr = ptr.next
        print("None")

    def insert(self, pos, e):
        node = DNode(e) # 삽입할 이중 연결 구조의 노드 생성
        before = self.getNode(pos-1) # 삽입할 위치 이전 노드 탐색
        if before == None: # node의 다음 노드가 현재 head가 되고, 그 노드의 prev를 node로 수정하며, 마지막으로 머리노드 head를 노드로 변경
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self.head = node
        else:
            before.append(node)

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None: # 머리노드를 삭제하면, head가 다음노드로 변경됨
                self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return before
        else:
            return before.popNext()
        