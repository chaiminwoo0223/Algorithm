# 0-1 배낭 채우기(브루트포스 알고리즘)
def Knapsack01_BF(wgt, val, W):
    n = len(wgt) # 전체 물건의 수
    bestVal = 0 # 배낭의 최대 가치

    for i in range(2**n): # 부분집합의 수는 2^n이므로, i에 0부터 2^n-1까지를 순서대로 대입함
        s = [0]*n
        for d in range(n): # i를 이진수로 변환했을 때, 각 자리의 수를 리스트에 저장(역순으로)
            s[d] = i % 2
            i = i // 2

        sumVal = 0
        sumWgt = 0
        for d in range(n):
            if s[d] == 1:
                sumWgt += wgt[d] # 물건의 총 무게
                sumVal += val[d] # 물건의 총 가치

        if sumWgt <= W:
            if sumVal > bestVal: # 가치합이 최대 가치보다 크면, 최대 가치 갱신
                bestVal = sumVal
    return bestVal # 최대 가치 반환

weight = [10, 20, 30, 25, 35] # 물건별 무게
value = [60, 100, 120, 70, 85] # 물건별 가치
print(Knapsack01_BF(weight, value, 80))
