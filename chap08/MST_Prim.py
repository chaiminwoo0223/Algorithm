# 프림의 최소 신장 트리 알고리즘
def MSTPrim(vertex, edge): # 정점 리스트 vertex, 인접 행렬 edge
    n = len(vertex)
    dist = [INF]*n # dist 배열 초기화(시작 정점만 0이고, 나머지는 모두 INF입니다.)
    dist[0] = 0 # 시작 정점
    selected = [False]*n # selected 배열 초기화

    for _ in range(n): # n개의 정점을 MST에 추가하면 종료됨
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')
        for v in range(n):
            if edge[u][v] != INF and not selected[v]:
                if edge[u][v] < dist[v]: # (u, v)가 dist[v]보다 작으면
                    dist[v] = edge[u][v] # dist[v] 갱신
        print(": ", dist)

# MST에 포함되지 않은 최소 dist의 정점 찾기
def getMinVertex(dist, selected):
    minv = 0
    mindist = INF

    for v in range(len(dist)): 
        if selected[v] == False and dist[v] < mindist: # MST에 포함되지 않은 정점 중에서, 최소 dist를 갖는 정점의 인덱스 minv를 구함
            mindist = dist[v]
            minv = v
    return minv

INF = 999
vertex = ['A', 'B', 'C', 'D', 'E', 'F'] # 정점 리스트
edge = [[0, 25, INF, 12, INF, INF],
        [25, 0, 36, 10, 17, INF],
        [INF, 36, 0, INF, 19, 14],
        [12, 10, INF, 0, INF, 22],
        [INF, 17, 19, INF, 0, 20],
        [INF, INF, 14, 22, 20, 0]] # 인접 행렬
MSTPrim(vertex, edge)
