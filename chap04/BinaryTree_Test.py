# 이진 트리의 테스트 프로그램
from BinaryTree import BNode, inorder, preorder, postorder, levelorder, count_node, calc_height

d = BNode('D', None, None)
e = BNode('E', None, None)
b = BNode('B', d, e)
f = BNode('F', None, None)
c = BNode('C', f, None)
root = BNode('A', b, c)

print("\n In-Order: ", end=' '); inorder(root)
print("\n Pre-Order: ", end=' '); preorder(root)
print("\n Post-Order: ", end=' '); postorder(root)
print("\n Level-Order: ", end=' '); levelorder(root)
print("\n 노드의 개수 = %d개" % count_node(root))
print(" 트리의 높이 = %d개" % calc_height(root))
