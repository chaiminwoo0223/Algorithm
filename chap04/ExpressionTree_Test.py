# 수식 트리 테스트 프로그램
from BinaryTree import inorder, preorder, postorder
from ExpressionTree import evaluate, buildETree

str = input("입력(후위표기): ") # 후위표기식 입력
expr = str.split() # 토큰 리스트로 변환
print("토큰분리(expr): ", expr)
root = buildETree(expr) # 후위표기식을 수식트리로 만들고, 루트를 반환

print("\n 전위순회: ", end=' '); preorder(root)
print("\n 중위순회: ", end=''); inorder(root)
print("\n 후위순회: ", end=''); postorder(root)
print("\n 계산결과: ", evaluate(root)); # 수식 트리 계산
print()
