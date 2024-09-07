# 리스트의 sort() 메소드
elements = [6, 3, 7, 4, 9, 1, 5, 2, 8]
print("원본:", elements)

elements.sort()
print("오름차순 정렬:", [element for element in elements])

elements = [6, 3, 7, 4, 9, 1, 5, 2, 8]
elements.sort(reverse=True)
print("내림차순 정렬:", [element for element in elements])
