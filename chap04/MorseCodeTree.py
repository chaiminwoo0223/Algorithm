# 결정 트리
from BinaryTree import BNode

# 영어 대문자에 대한 모스 코드 표
table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
         ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
         ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), 
         ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), 
         ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), 
         ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), 
         ('Y', '-.--'), ('Z', '--..')]

# 모스 코드 디코딩을 위한 결정 트리 만들기
def make_morse_tree():
    root = BNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left == None:
                    node.left = BNode(None, None, None)
                node = node.left
            elif c == '-':
                if node.right == None:
                    node.right = BNode(None, None, None)
                node = node.right
        node.data = tp[0]
    return root

# 모스 코드 인코딩 함수
def encode(ch):
    idx = ord(ch) - ord('A') # 리스트에서 해당 문자의 인덱스
    return table[idx][1]

# 결정 트리를 이용한 디코딩 함수
def decode(root, code):
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
    return node.data
