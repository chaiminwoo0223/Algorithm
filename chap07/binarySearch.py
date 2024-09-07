# 이진 탐색 알고리즘
def binary_search(A, key, low, high):
    if low <= high: # 항목들이 남아 있으면(종료 조건)
        middle = (low + high) // 2 # middle 계산
        if key == A[middle]: # 탐색 성공
            return middle
        elif key < A[middle]:
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
    return -1 # 실패

def binary_search_iter(A, key, low, high):
    while (low <= high): # 항목들이 남아 있으면(종료 조건)
        middle = (low + high) // 2 # middle 계산
        if key == A[middle]: # 탐색 성공
            return middle
        elif key < A[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1 # 실패

data = [3, 5, 8, 15, 16, 19, 22, 25, 27, 31, 32, 36, 39, 40, 43, 45]
print(binary_search(data, 27, 0, len(data)-1))
print(binary_search_iter(data, 27, 0, len(data)-1))
