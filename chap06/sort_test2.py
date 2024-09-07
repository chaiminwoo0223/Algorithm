# 파이썬의 내장함수 sorted()
elements = [6, 3, 7, 4, 9, 1, 5, 2, 8]
print("원본:", elements)
result = sorted(elements)
print("오름차순 정렬:", result)

print("원본:", elements) # 원래의 리스트(elements)가 수정되지 않음
result = sorted(elements, reverse=True)
print("내림차순 정렬:", result)
