# DFS를 이용한 신장트리(인접행렬 방식)
def ST_DFS(vtx, edge, s, visited):
    visited[s] = True

    for v in range(len(vtx)):
        if edge[s][v] != 0: 
            if visited[v] == False: # 방문하지 않은 s의 이웃 정점 v가 있으면
                print("(", vtx[s], vtx[v], ")", end=' ') # 간선 (s, v)를 신장트리에 추가하고
                ST_DFS(vtx, edge, v, visited) # v를 시작으로 다시 DFS 진행

vtx = ['U', 'V', 'W', 'X', 'Y'] # 정점 리스트
edge = [[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0]] # 인접 행렬
visited = [False]*len(vtx) # 길이가 정점 수와 같은 False 리스트를 만듦
print("ST_DFS(출발:U):", end=' ')
ST_DFS(vtx, edge, 0, visited) 
print()
