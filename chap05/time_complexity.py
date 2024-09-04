# 리스트에서 최댓값을 찾는 알고리즘
def find_max(A):
    n = len(A) # 입력의 크기
    max = A[0] # max 초기화
    for i in range(n): # 최댓값 비교
        if A[i] > max:
            max = A[i]
    return max

nums = list(map(int, input().split()))
print(find_max(nums))
