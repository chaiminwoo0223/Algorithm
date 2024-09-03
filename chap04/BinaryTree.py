# 이진 트리
from ArrayQueue import ArrayQueue

# 이진 트리를 위한 노드 클래스
class BNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None

# 이진 트리의 전위순회
def preorder(n):
    if n is not None:
        print("(", end=' ')
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)
        print(")", end=' ')

# 이진 트리의 중위순회
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

# 이진 트리의 후위순회
def postorder(n):
    if n is not None:
        postorder(n.right)
        postorder(n.left)
        print(n.data, end=' ')

# 이진 트리의 레벨순회
def levelorder(root):
    queue = ArrayQueue() # 큐 객체 초기화
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

# 이진 트리의 노드 수 구하기
def count_node(n):
    if n is None: # n이 None이면, 공백 트리 -> 0
        return 0
    else: # 좌우 서브 트리 노드 수의 합 + 1(순환)
        return count_node(n.left) + count_node(n.right) + 1 

# 이진 트리의 높이 구하기
def calc_height(n):
    if n is None: # n이 None이면, 공백 트리 -> 0
        return 0
    hLeft = calc_height(n.left) # 왼쪽 서브 트리 높이
    hRight = calc_height(n.right) # 오른쪽 서브 트리 높이
    if hLeft > hRight: # 더 큰 값 + 1
        return hLeft + 1
    else:
        return hRight + 1 
