# 반복 구조의 팩토리얼 함수
def factorial_iter(n):
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

print(factorial_iter(10))

# 순환 구조의 팩토리얼 함수
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))
