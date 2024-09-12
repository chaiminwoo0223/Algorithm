# 병합 정렬 알고리즘
def merge_sort(A, left, right): # A[left ... right]를 오름차순으로 정렬
    if left < right: # 항목이 2개 이상인 경우
        mid = (left + right) // 2 # 중간값 계산
        merge_sort(A, left, mid) # 왼쪽 부분 리스트 병합 정렬
        merge_sort(A, mid+1, right) # 오른쪽 부분 리스트 병합 정렬
        merge(A, left, mid, right) # 마지막으로 정렬된 두 부분 리스트를 병합

# 병합 알고리즘
def merge(A, left, mid, right):
    sorted = [0]*len(A)  # 임시 리스트 생성
    k = left  # 병합을 위한 임시 리스트의 인덱스
    i = left  # 왼쪽 리스트의 인덱스
    j = mid + 1  # 오른쪽 리스트의 인덱스

    # 병합 과정
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i += 1
        else:
            sorted[k] = A[j]
            j += 1
        k += 1

    # 왼쪽 부분 리스트의 남은 요소 처리
    while i <= mid:
        sorted[k] = A[i]
        i += 1
        k += 1

    # 오른쪽 부분 리스트의 남은 요소 처리
    while j <= right:
        sorted[k] = A[j]
        j += 1
        k += 1

    # 원래 리스트에 병합된 결과 복사
    A[left:right+1] = sorted[left:right+1]

data = [38, 27, 43, 3, 9, 82, 10]
print("원래 리스트:", data)
merge_sort(data, 0, len(data)-1)
print("정렬된 리스트:", data)
