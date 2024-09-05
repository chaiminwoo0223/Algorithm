# 삽입 정렬 알고리즘
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i] # 삽입할 요소를 미리 key에 저장
        j = i-1
        while j >= 0 and A[j] > key: # i-1부터 비교하여 앞으로 진행하는데, 이 요소가 key보다 크면 뒤로 한 칸 옮김(핵심)
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key # j+1이 A[i]가 삽입될 위치
        print("Step %2d =" %(i+1), A)

data = [6, 3, 7, 4, 9, 1, 5, 2, 8]
print("Original:", data)
insertion_sort(data)
print("Selection:", data)
