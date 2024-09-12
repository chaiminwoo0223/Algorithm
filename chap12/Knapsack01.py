# 0-1 배낭 채우기(분할 정복)
def knapSack_dc(W, wt, val, n):
    if n == 0 or W == 0: # 기반 상황
        return 0
    if wt[n-1] > W: # 마지막 물건을 넣을 용량이 부족한 경우
        return knapSack_dc(W, wt, val, n-1)
    else:
        valWith = val[n-1] + knapSack_dc(W-wt[n-1], wt, val, n-1) # 마지막 물건을 넣는 경우
        valWithout = knapSack_dc(W, wt, val, n-1) # 그렇지 않은 경우
        return max(valWith, valWithout)
    
# 0-1 배낭 채우기(다이나믹 프로그래밍)
def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W+1)] for x in range(n+1)] # (n+1)x(W+1) 크기의 2차원 배열을 생성하고 모든 요소를 0으로 초기화
    for i in range(1, n+1): # 위에서 아래로 진행
        for w in range(1, W+1): # 좌에서 우로 진행
            if wt[i-1] > w: # i번째 물건을 넣을 수 없는 경우(용량 초과)
                A[i][w] = A[i-1][w]
            else: # i번째 물건을 넣을 수 있는 경우
                valWith = val[i-1] + A[i-1][w-wt[i-1]] # 넣는 경우
                valWithout = A[i-1][w] # 빼는 경우
                A[i][w] = max(valWith, valWithout)
    return A[n][W]

val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
n = len(val)
print("0-1 배낭문제(분할 정복):", knapSack_dc(W, wt, val, n))
print("0-1 배낭문제(다이나믹 프로그래밍):", knapSack_dp(W, wt, val, n))
