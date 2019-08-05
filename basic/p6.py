'''
연속데이터(시퀀스 타입)
    > 집합  : set() -> 순서 없음 : {값, 값, 값, ...} 형태 => 중복 제거 후 리스트로 변환해서 처리
                       교집합, 합집합, 차집합 -> but, 느려서 pandas에서 해결
'''

a = 'helloworld'

# 중복 제거
b = set(a)
print(b)        # {'o', 'e', 'w', 'r', 'l', 'd', 'h'}

# 리스트 변환
print(list(b))  # ['o', 'l', 'r', 'e', 'w', 'd', 'h']

a = set([1, 3, 5, 7, 9, 2, 6, 5])
b = set([2, 4, 6, 8, 1, 5, 4])
# 교집합
print(a.intersection(b))
# 합집합
print(a.union(b))
# 차집합(방향성 중요 / A-B vs B-A)
print(a.difference(b))
print(b.difference(a))

