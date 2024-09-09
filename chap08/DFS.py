# 깊이 우선 탐색(인접행렬 방식)
def DFS(vtx, edge, s, visited): # 정점 리스트 vtx, 인접 행렬 edge, 시작 정점 s, 방문 리스트 visted
    print(vtx[s], end=' ')
    visited[s] = True # 현재 정점 s는 방문했기 때문에, visited를 True로 갱신

    for v in range(len(vtx)):
        if edge[s][v] != 0:
            if visited[v] == False: # 방문하지 않은 이웃 정점 v가 있으면
                DFS(vtx, edge, v, visited) # 그 정점을 시작으로 다시 DFS 호출

# 깊이 우선 탐색 테스트 프로그램
vtx = ['U', 'V', 'W', 'X', 'Y'] # 정점 리스트
edge = [[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0]] # 인접 행렬
visited = [False]*len(vtx) # 길이가 정점 수와 같은 False 리스트를 만듦
print("DFS(출발:U):", end=' ')
DFS(vtx, edge, 0, visited) 
print()
