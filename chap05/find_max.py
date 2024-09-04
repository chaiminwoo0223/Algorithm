# 최댓값 찾기 알고리즘
def find_max(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

num1, num2, num3 = map(int, input().split())
print(find_max(num1, num2, num3))
