# 분할정복을 이용한 k번째 작은 수 찾기
def quick_select(A, left, right, k):
    pos = partition(A, left, right) # A에서 pivot의 인덱스
    if pos == left + k - 1:
        return A[pos]
    elif pos > left + k - 1:
        return quick_select(A, left, pos-1, k)
    else:
        return quick_select(A, pos+1, right, k-(pos+1-left))

# 분할 알고리즘
def partition(A, left, right):
    pivot = A[left]
    low = left + 1
    high = right

    while low <= high:
        # 양쪽에서 조건에 맞지 않는 요소를 찾는 과정
        while low <= right and A[low] <= pivot: # A[low] <= pivot이면 low를 오른쪽으로 진행
            low += 1
        while high >= left and A[high] > pivot: # A[high] > pivot이면 high를 왼쪽으로 진행
            high -= 1
        if low < high: # 역전이 아니면 두 레코드 교환
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left] # pivot과 high를 교환
    return high # pivot의 인덱스 high를 반환

data = [6, 5, 7, 9, 18, 3, 8] # 입력 리스트
print("k번째 작은 수:", quick_select(data, 0, len(data)-1, 4))
