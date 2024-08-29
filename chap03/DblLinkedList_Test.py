# DblLinkedList 테스트
from DblLinkedList import DblLinkedList

s = DblLinkedList()
s.display("연결리스트(초기): ")
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("연결리스트(삽입x5): ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("연결리스트(삭제x3): ")
