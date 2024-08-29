# LinkedList와 파이썬 리스트 비교
from LinkedList import LinkedList

s = LinkedList()
s.display("연결리스트(초기): ")
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("연결리스트(삽입x5): ")
s.replace(2, 90)
s.display("연결리스트(교체x1): ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("연결리스트(삭제x3): ")

l = []
print("파이썬 list(초기):", l)
l.insert(0, 10)
l.insert(0, 20)
l.insert(1, 30)
l.insert(len(l), 40)
l.insert(2, 50)
print("파이썬 list(삽입x5):", l)
l[2] = 90
print("파이썬 list(교체x1):", l)
l.pop(2)
l.pop(3)
l.pop(0)
print("파이썬 list(삭제x3):", l)
