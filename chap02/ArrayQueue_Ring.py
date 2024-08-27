# 링 버퍼의 테스트 프로그램
# 링 버퍼: 가장 최근에 들어온 데이터는 저장하고, 오래된 데이터는 삭제하는 것
from ArrayQueue import ArrayQueue

q = ArrayQueue(8)

q.display("초기 상태")
for i in range(6):
    q.enqueue2(i)
q.display("삽입 0-5")

q.enqueue2(6) # 포화 상태
q.display("삽입 6") 

q.enqueue2(7) # 0 삭제
q.display("삽입 7") 

q.enqueue2(8) # 1 삭제
q.enqueue2(9) # 2 삭제
q.display("삽입 8,9")

q.dequeue()
q.dequeue()
q.display("삭제 x2")