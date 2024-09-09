# 너비 우선 탐색
from queue import Queue

# 너비 우선 탐색(인접 리스트 방식)
def BFS(vtx, aList, s): # 정점 리스트 vtx, 인접 리스트 aList, 시작 정점 s
    n = len(vtx) # 그래프의 정점 수
    visited = [False]*n # 방문 확인을 위한 리스트
    Q = Queue() # 큐를 만들고
    Q.put(s) # 시작 정점 s만 큐에 넣음
    visited[s] = True # s는 방문했다고 표시

    while not Q.empty():
        s = Q.get() # 큐에서 정점 s를 꺼내고
        print(vtx[s], end=' ')
        for v in aList[s]: # s의 인접 정점들 중에서
            if visited[v] == False: # 아직 방문하지 않은 정점들을
                Q.put(v) # 큐에 모두 삽입
                visited[v] = True # "방문"했다고 표시

vtx = ['U', 'V', 'W', 'X', 'Y'] # 정점 리스트
aList = [[1, 2],
         [0, 2, 3],
         [0, 1, 4],
         [1],
         [2]] # 인접 리스트
print("BFS(출발:U):", end=' ')
BFS(vtx, aList, 0)
print()