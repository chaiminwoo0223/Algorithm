# 인코딩과 디코딩 테스트 프로그램
from MorseCodeTree import make_morse_tree, encode, decode

morseCodeTree = make_morse_tree()
str = input("입력 문장: ")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print("Morse Code: ", mlist)
print("Decoding: ", end='')
for code in mlist:
    ch = decode(morseCodeTree, code)
    print(ch, end='')
print()
