# 분할 가능한 배낭 채우기(그리디 알고리즘)
def KnapSackFrac(wgt, val, W): # 물건들은 단위 무게당 가격의 내림차순으로 정렬되어 있어야 함
    bestVal = 0 # 최대 가치
    for i in range(len(wgt)): # 단가가 높은 물건부터 처리
        if W <= 0: # 용량이 다 찾으면 채우기 종료
            break
        if W >= wgt[i]: # 물건 전체를 넣을 수 있으면
            W -= wgt[i] # 남은 용량 W를 갱신하고(물건 전체를 넣고)
            bestVal += val[i] # 최대 가치를 증가시킴
        else:
            fraction = W / wgt[i] # 최대 비율을 계산
            bestVal += val[i]*fraction # 최대 가치를 증가시킴
            break
    return bestVal # 최대 가치 반환

weight = [12, 10, 8]
value = [120, 80, 60]
W = 18
print("Fractional Knapsack(18):", KnapSackFrac(weight, value, W))
