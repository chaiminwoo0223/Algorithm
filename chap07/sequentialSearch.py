# 순차 탐색 알고리즘
def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key: # 탐색 성공하면
            return i # 인덱스 반환
    return -1 # 실패

# 교환하기 전략이 추가된 순차 탐색 알고리즘
def sequential_search_transpose(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            if i > low: # 맨 처음 요소가 아니면
                A[i], A[i-1] = A[i-1], A[i] # 교환하기(transpose)
                i = i - 1 # 한 칸 앞으로 왔음
            return i # 인덱스 반환
    return -1 # 실패

data = [6, 3, 7, 4, 9, 1, 5, 2, 8]
print(sequential_search(data, 9, 0, len(data)-1))
print(sequential_search_transpose(data, 9, 0, len(data)-1))
