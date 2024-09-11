# 거듭제곱 구하기
import time

# x의 n 거듭제곱 구하기(억지기법)
def slow_power(x, n): # 반복으로 x^n을 구하는 함수
    result = 1.0
    for _ in range(n):
        result = result * x
    return result

# x의 n 거듭제곱 구하기(축소정복)
def power(x, n):
    if n == 1: # 종료 조건
        return x # 모든 수의 1승은 그 수
    elif (n % 2) == 0: # n이 짝수이면
        return power(x*x, n//2)
    else: # n이 홀수이면
        return x * power(x*x, (n-1)//2)
    
print("억지기법(2**500) =", slow_power(2.0, 500))
print("축소정복(2**500) =", power(2.0, 500))

t1 = time.time()
for i in range(100000): slow_power(2.0, 500) # 억지기법 10만 
t2 = time.time()
for i in range(100000): power(2.0, 500) # 축소정복 10만
t3 = time.time()

print("억지기법 시간...", t2-t1)
print("축소정복 시간...", t3-t2)
