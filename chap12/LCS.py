# LCS의 길이(분할 정복)
def lcs_recur(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_recur(X, Y, m-1, n-1)
    else:
        return max(lcs_recur(X, Y, m, n-1), lcs_recur(X, Y, m-1, n))
    
# LCS의 길이(다이나믹 프로그래밍)
def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for _ in range(m+1)] # 테이블 준비

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0: # 기반 상황
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: # 마지막 글자가 같으면
                L[i][j] = L[i-1][j-1] + 1
            else: # 마지막 글자가 다르면
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n] # 최종 결과

X = "GAME OVER"
Y = "HELLO WORLD"
print("X =", X)
print("Y =", Y)
print("LCS(분할 정복):", lcs_recur(X, Y, len(X), len(Y)))
print("LCS(다이나믹 프로그래밍):", lcs_dp(X, Y))
