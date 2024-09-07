# 퀵 정렬 알고리즘
def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right) # 피벗을 중심으로 리스트를 두 부분으로 분할하고, 피벗의 위치 q를 구함
        quick_sort(A, left, q-1) # 왼쪽 부분 리스트 정렬
        quick_sort(A, q+1, right) # 오른쪽 부분 리스트 정렬

# 분할 알고리즘
def partition(A, left, right):
    pivot = A[left]
    low = left + 1
    high = right

    while (low < high): # low와 high가 역전되지 않는 한 반복
        # 양쪽에서 조건에 맞지 않는 요소를 찾는 과정
        while low <= right and A[low] <= pivot: # A[low] <= pivot이면 low를 오른쪽으로 진행
            low += 1
        while high >= left and A[high] > pivot: # A[high] > pivot이면 high를 왼쪽으로 진행
            high -= 1
        if low < high: # 역전이 아니면 두 레코드 교환
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left] # pivot과 high를 교환
    return high # pivot의 인덱스 high를 반환

data = [5, 3, 8, 4, 9, 1, 6, 2, 7] # 입력 리스트
print("Original:", data)
quick_sort(data, 0, len(data)-1) # 퀵 정렬
print("QuickSort:", data)
