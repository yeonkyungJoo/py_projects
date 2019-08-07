# 내장함수
# 파일처리, 파일 덤프
'''
mode options
r : 읽기
w : 쓰기
b : 바이너리 모드
+ : 반대 속성 추가 / r+ == rw
a : append (기존 내용에 추가)
'''
f = open('f1.txt', 'w')
for n in range(10) :
    f.write('%d 라인 line 12!@\n' % n)
f.close()

f = open('f1.txt', 'r')
print(f.read())
f.close()

# I/O에서는 열었으면 반드시 닫아야 한다!
# 간혹 누락시키는 경우가 존재한다 -> 원천적으로 해결하는 것이 좋다 -> 자동으로 닫히게 한다
# with문 ~ :
with open('f1.txt', 'r') as f :
    print(f.read())

# 외장함수
# 피클 -> 자료구조를 유지해서 덤프, 로드
# 머신러닝에서도 피클을 customize해서 지원
import pickle as p
data = {
    1 : [1, 2, 3, 4],
    2 : {'name' : '컴퓨터'},
    3 : (5, 6, 7, 8)
}
# 덤프
with open('data.p', 'wb') as f1 :
    p.dump(data, f1, p.HIGHEST_PROTOCOL)

# 로드
with open('data.p', 'rb') as f2 :
    tmp = p.load(f2)
    print( tmp, type(tmp) )

# os 모듈
import os
# 현재 프로젝트 경로
print( os.getcwd() )
# 제시된 디렉토리에 존재하는 모든 파일, 디렉토리들을 리스트로 나열
print( os.listdir(os.getcwd()) )