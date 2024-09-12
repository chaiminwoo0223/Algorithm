# 피보나치 수열(메모이제이션 이용)
def fib_dp_mem(n):
    if mem[n] is None:
        if n < 2:
            mem[n] = n
        else:
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n]

# 피보나치 수열(테이블화 이용)
def fib_dp_tab(n):
    f = [None]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = 15
mem = [None]*(n+1) # 메모이제이션 리스트
print("Fibonacci(15) 메모이제이션:", fib_dp_mem(n))
print("Fibonacci(15) 테이블화:", fib_dp_tab(n))
