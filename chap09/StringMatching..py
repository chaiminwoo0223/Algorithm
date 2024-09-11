# 문자열 매칭
def string_matching(T, P): # T: 입력 문자열(텍스트), P: 탐색 패턴
    n = len(T) # n: 텍스트의 길이
    m = len(P) # m: 패턴의 길이

    for i in range(n-m+1): # 텍스트의 위치(i)는 0부터 n-m까지만 진행되어야 함
        j = 0
        while j < m and P[j] == T[i+j]: # 현재 텍스트 위치(i)에서 패턴의 첫문자(j=0)부터 하니씩 비교함
            j += 1
        if j == m: # 만약, 맨 끝까지 일치하면
            return i # 매칭 성공
    return -1 # 매칭 실패

print(string_matching("HELLO WORLD", "LO"))
print(string_matching("HELLO WORLD", "HI"))
