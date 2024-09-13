# 문자열 탐색키에 대한 해시 함수
def hashFnStr(key):
    sum = 0
    for c in key:
        sum += ord(c) 
    return sum % M 

# 나머지 연산을 이용한 해시 함수
def hashFn(key):
    return key % M

# 선형 조사법의 삽입 알고리즘
def lp_insert(key):
    id = hashFn(key)
    count = M
    while count > 0 and (table[id] != None and table[id] != -1):
        id = (id + 1 + M) % M
        count -= 1
    if count > 0:
        table[id] = key
    return

# 선형 조사법의 탐색 알고리즘
def lp_search(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:
            return None
        if table[id] == key:
            return table[id]
        id = (id + 1 + M) % M
        count -= 1
    return None

# 선형 조사법의 삭제 알고리즘
def lp_delete(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:
            return
        if table[id] != -1 and table[id] == key:
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1

M = 13
table = [None]*M # 크기가 M인 해시 테이블 준비

print("최초:", table)
lp_insert(45); print("45 삽입:", table)
lp_insert(27); print("27 삽입:", table)
lp_insert(88); print("88 삽입:", table)
lp_insert(9); print("9 삽입:", table)
lp_insert(71); print("71 삽입:", table)
lp_insert(60); print("60 삽입:", table)
lp_insert(46); print("46 삽입:", table)
lp_insert(38); print("38 삽입:", table)
lp_insert(24); print("24 삽입:", table)
lp_delete(60); print("60 삭제:", table)
print("46 탐색:", lp_search(46))
