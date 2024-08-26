# 하노이의 탑
def hanoi_tower(n, fr, tmp, to): # 원판의 수, 시작 막대, 임시 막대, 목표 막대
    if (n == 1):
        print("원판 1: %s --> %s" %(fr, to)) # 순환 호출을 멈추는 부분: 원판이 하나라면 바로 이동
    else:
        hanoi_tower(n-1, fr, to, tmp) # 1단계
        print("원판 %d: %s --> %s" %(n, fr, to)) # 2단계
        hanoi_tower(n-1, tmp, fr, to) # 3단계

hanoi_tower(4, 'A', 'B', 'C')
