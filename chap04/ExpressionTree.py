# 수식 트리
from BinaryTree import BNode

# 수식 트리 계산 함수
def evaluate(node):
    if node is None: # 공백 트리 -> 0 반환
        return 0
    elif node.isLeaf(): # 리프 노드 -> 피연산자 반환
        return node.data
    else: # 루트 or 중간 노드 -> 연산자 반환
        op1 = evaluate(node.left) # 왼쪽 서브 트리 계산
        op2 = evaluate(node.right) # 오른쪽 서브 트리 계산
        if node.data == '+':
            return op1 + op2
        elif node.data == '-':
            return op1 - op2
        elif node.data == '*':
            return op1 * op2
        elif node.data == '/':
            return op1 / op2
        
# 후위표기 수식을 이용한 수식 트리 만들기
def buildETree(expr): # 후위표기 수식을 전달
    if len(expr) == 0:
        return None
    token = expr.pop() # 후위순회는 뒤에서 앞으로 처리, pop()으로 맨 뒤의 요소를 꺼냄.
    if token in "+-*/":
        node = BNode(token)
        node.right = buildETree(expr)
        node.left = buildETree(expr)
        return node
    else:
        return BNode(float(token)) # 피연산자이면 리프 노드이므로, 노드를 만들어 반환
