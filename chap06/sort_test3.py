# 공간상의 점들을 정렬하자!
import math

data = [(62, 88, 81), (50, 3, 31), (86, 53, 42), (73, 47, 4), (89, 9, 8), 
        (47, 88, 55), (19, 18, 20), (15, 1, 88), (90, 6, 60), (41, 92, 19)]

print("data:", data)
x_inc = sorted(data, key = lambda p : p[0]) # 기준1: x값의 오름차순 정렬
print("x_inc:", x_inc)
y_inc = sorted(x_inc, key = lambda p : p[1], reverse = True) # 기준2: y값의 내림차순 정렬
print("y_inc:", y_inc)
magni = sorted(y_inc, key = lambda p : math.sqrt(p[0]*p[0]+p[1]*p[1]+p[2]*p[2])) # 기준3: 크기의 오름차순 정렬
print("magni:", magni)
