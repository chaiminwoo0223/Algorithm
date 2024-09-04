# 리스트에서 어떤 값을 찾는 알고리즘
def find_key(A, key):
    n = len(A) # 입력의 크기
    for i in range(n): # 순차탐색
        if A[i] == key:
            return i # 성공
    return -1 # 실패

print(find_key([i for i in range(1, 10)], 1)) # 최선
print(find_key([i for i in range(1, 10)], 4)) # 평균
print(find_key([i for i in range(1, 10)], 9)) # 최악
print(find_key([i for i in range(1, 10)], 10)) # 최악(-1)
