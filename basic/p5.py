'''
연속데이터(시퀀스 타입)
    > 튜플  : () -> 수정 불가(immutable), 
                    값을 묶는다(관계없는 데이터들을 묶는다),
                    순서 존재
                 => 함수에서 여러 값을 리턴할 때 튜플로 적용되서 리턴된다
                    멤버가 1개이면 -> (1, ) 만약 (1) <- 이것은 값1 소괄호
'''

tu = ()
print(tu, len(tu), type(tu))  # () 0 <class 'tuple'>
tu = tuple()
print(tu, len(tu), type(tu))  # () 0 <class 'tuple'>

# 인덱싱, 슬라이싱, 정방향/역방향 모두 적용
tu = (1, 2, 3, 4)
print(tu[0])
print(tu[:2])
print(tu[-1])
a = (5, 6, 7, 8)
print(tu + a) # 이어붙이기 가능
