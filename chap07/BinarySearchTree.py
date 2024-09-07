# 이진 탐색 트리를 위한 노드 클래스
class BSTNode:
    def __init__(self, key, value):
        self.key = key # 키(key)
        self.value = value # 값(value)
        self.left = None # 왼쪽 자식에 대한 링크
        self.right = None # 오른쪽 자식에 대한 링크

    def __str__(self):
        return f"({self.key}:{self.value})"  # 출력 형식 지정

# 이진 탐색 트리의 탐색 연산(순환 구조)
def search_bst(n, key): # n을 루트로 가지는 이진 탐색 트리에서 key인 노드를 찾는 순환 함수
    if n == None: # n이 None이면 공백 트리이므로 None을 반환
        return None
    elif key == n.key: # n의 key가 탐색키와 같으면 n을 반환
        return n
    elif key < n.key: # n의 key가 탐색키보다 크다면 왼쪽 서브 트리 반환
        return search_bst(n.left, key) 
    else: # n의 key가 탐색키보다 작다면 오른쪽 서브 트리 반환
        return search_bst(n.right, key)
    
# 이진 탐색 트리의 값을 이용한 탐색(전위 순회)
def search_value_bst(n, value): # n을 루트로 가지는 이진 탐색 트리에서 value인 노드를 찾는 순환 함수(전위 순회)
    if n == None: # n이 None이면 공백 트리이므로 None을 반환
        return None
    elif value == n.value: # n의 value가 탐색하는 값과 같으면 n을 반환
        return n
    elif search_value_bst(n.left, value) is not None: # 왼쪽 서브 트리 탐색 후 결과 반환
        return search_value_bst(n.left, value)
    else: # 오른쪽 서브 트리 탐색 후 결과 반환
        return search_value_bst(n.right, value)
    
# 이진 탐색 트리의 삽입 연산(순환 구조)
def insert_bst(root, node):
    if root == None: # 공백 노드에 도달하면 해당 위치에 삽입
        return node # node를 반환(이 노드가 현재 root 위치에 감)
    if node.key == root.key: # 동일한 키는 허용하지 않음
        return root # root를 반환(root는 변화 없음)
    if node.key < root.key: # 왼쪽 서브 트리에 넣어야 하는 경우
        root.left = insert_bst(root.left, node) # root의 왼쪽 자식을 루트에 삽입하고, 왼쪽 자식 갱신
    else: # 오른쪽 서브 트리에 넣어야 하는 경우
        root.right = insert_bst(root.right, node) # root의 오른쪽 자식을 루트에 삽입하고, 오른쪽 자식 갱신
    return root # root를 반환(root는 변화 없음)

# 이진 탐색 트리의 삭제 연산(순환 구조)
def delete_bst(root, key):
    if root == None: # 공백 트리
        return root
    if key < root.key: # key가 루트보다 작다면
        root.left = delete_bst(root.left, key) # 왼쪽 서브 트리에서 삭제를 계속 진행하고, 자식이 갱신될 수 있으므로 반환된 값으로 자식을 갱신
    elif key > root.key: # key가 루트보다 크다면
        root.right = delete_bst(root.right, key) # 오른쪽 서브 트리에서 삭제를 계속 진행하고, 자식이 갱신될 수 있으므로 반환된 값으로 자식을 갱신
    else: # key가 루트의 key와 같으면 root를 삭제
        # 리프 노드 또는 오른쪽 자식만 있는 경우
        if root.left == None:
            return root.right # 오른쪽 자식을 반환
        # 왼쪽 자식만 있는 경우
        if root.right == None: 
            return root.left # 왼쪽 자식을 반환
        # 두 자식이 모두 있는 경우
        succ = root.right # 후계자를 찾고(오른쪽 서브 트리 최소 노드)
        while (succ.left != None):
            succ = succ.left
        # 후계자의 key와 value를 복사하고, 후계자를 삭제
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key) # 후계자 삭제(오른쪽 서브 트리에서 후계자 key 값을 가진 노드를 삭제)
    return root

# 노드 출력 함수
def print_node(msg, n):
    print(msg, n if n != None else "탐색 실패")

# 전위 순회를 이용한 트리 출력 함수
def print_tree(msg, r):
    print(msg, end='')
    preorder(r)
    print()

# 이진 트리의 전위순회
def preorder(n):
    if n is not None:
        print("{", end='')
        print(f"({n.key}:{n.value})", end='')
        preorder(n.left)
        preorder(n.right)
        print("}", end='')

data = [(6, "여섯"), (8, "여덟"), (2, "둘"), (4, "넷"), (7, "일곱"), (5, "다섯"), (1, "하나"), (9, "아홉"), (3, "셋"), (0, "영")]
root = None # 루트 노드 초기화
for i in range(0, len(data)): # 노드 순서대로 추가하기
    root = insert_bst(root, BSTNode(data[i][0], data[i][1]))

# 최초의 트리 출력
print_tree("최초:", root)

# 탐색
n = search_bst(root, 3); print_node("search 3:", n)
n = search_bst(root, 8); print_node("search 8:", n)
n = search_bst(root, 0); print_node("search 0:", n)
n = search_bst(root, 10); print_node("search 10:", n)
n = search_value_bst(root, "둘"); print_node("search 둘:", n)
n = search_value_bst(root, "열"); print_node("search 열:", n)

# 삭제
root = delete_bst(root, 7); print_tree("delete 7: ", root)
root = delete_bst(root, 8); print_tree("delete 8: ", root)
root = delete_bst(root, 2); print_tree("delete 2: ", root)
root = delete_bst(root, 6); print_tree("delete 6: ", root)
