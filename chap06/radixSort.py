# 기수 정렬 알고리즘
from collections import deque
import random

def radix_sort(A):
    queues = [] # 버킷 리스트
    [queues.append(deque()) for _ in range(BUCKETS)] # BUCKETS 개의 큐를 만들어, 버킷 리스트 queues에 추가
    n = len(A) # 리스트 전체 수
    factor = 1 # 가장 낮은 자리부터 시작

    for d in range(DIGITS): # 각 자릿수에 대해 처리
        for i in range(n): # 모든 항목을 따라 큐에 삽입
            queues[(A[i]//factor)%BUCKETS].append(A[i])

        i = 0
        for b in range(BUCKETS): # 0번부터 모든 버킷에 저장된 요소를 순서대로 꺼내 입력
            while queues[b]:
                A[i] = queues[b].popleft()
                i += 1
            
        factor *= BUCKETS # 그다음 자릿수로 간다.
        print("step", d+1, A) # 처리과정 출력

BUCKETS = 10 # 10진법 사용
DIGITS = 4 # 최대 4자릿수 숫자를 정렬

data = [random.randint(1, 9999) for _ in range(10)] # 난수 10개로 이루어진 리스트 생성
radix_sort(data)
print("Radix:", data)
