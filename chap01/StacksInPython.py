# 문자열 역순 출력(파이썬 리스트 이용)
s = list()

msg = input("문자열 입력: ")
for c in msg:
    s.append(c)

print("문자열 출력: ", end='')
while len(s) > 0:
    print(s.pop(), end='')
print()

# 문자열 역순 출력(LifoQueue 이용)
import queue

s = queue.LifoQueue(maxsize=100)

msg = input("문자열 입력: ")
for c in msg:
    s.put(c)

print("문자열 출력: ", end='')
while not s.empty():
    print(s.get(), end='')
print()    
