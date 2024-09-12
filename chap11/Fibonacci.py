# 분할 정복을 이용한 피보나치 수열
def fib(n):
    if n == 0: return 0 # 정복: 0번째 달
    elif n == 1: return 1 # 정복: 1번째 달
    else: return fib(n-1) + fib(n-2)

# 행렬 거듭제곱을 이용한 피보나치 수열
def fib_mat(n):
    if n == 0: return 0 # 정복: 0번째 달
    elif n == 1: return 1 # 정복: 1번째 달
    mat = [[1, 1], [1, 0]] # 초기 피보나치 행렬
    result = powerMat(mat, n) # 축소정복 방식
    return result[0][1] # fib(n) 부분 반환

# 행렬 곱셈 함수
def multiplyMat(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

# 행렬 거듭제곱 함수
def powerMat(mat, n):
    if n == 1:
        return mat
    elif n % 2 == 0:
        half_pow = powerMat(mat, n//2)
        return multiplyMat(half_pow, half_pow)
    else:
        return multiplyMat(mat, powerMat(mat, n-1))

print("분할 정복을 이용한 피보나치 수열:", fib(15))
print("행렬 거듭제곱을 이용한 피보나치 수열:", fib_mat(15))
