# 단일데이터(단일 타입)
# 문자열(연속이지만, 단일로도 분류한다)
# 표기법
# '...', "...", """...""", '''...'''
# """...""", '''...''' 용도 : 여러 줄 표현할 때, 구조 유지용, 여러 줄 주석용
a = 'hi'
print(a)
a = "hi"
print(a)

# 혼용 표현
a = 'abcd"KKK"efg'
print(a)
a = 'abcd\'KKK\'efg' # 이스케이프 문자로 동일 기호를 내부에서 사용 가능
print(a)

# 여러 줄 표현
a = '''
abcd
ef
gh
'''
print(a)

"""
여러 줄 주석
"""

# 문자열 더하기 (이어 붙이기) <-> 문자열 안에 문자열(포맷팅)
a = 'hello '
b = 'lunch'
print(a+b)

# 문자열 반복
print('1'*10)

# 인덱싱(indexing) : 문자열에서 특정 문자를 획득하는 방식
# -> '차원 축소'의 의미
# 문법 : 변수명[인덱스(정방향 or 역방향)] / 정방향, 역방향 선택 기준은 '가까운 쪽'
a = '0123456789'
# 2를 출력
print(a[2])
print(a[-8])

# 슬라이싱 : 데이터에서 범위에 해당되는 데이터를 획득
# -> '차원 유지'의 의미
# 문법 : 변수명[시작 인덱스:끝 인덱스:step(자르는 간격, 생략하면 1)]
# a를 카피
print(a[:])
# 1~8 출력
# 뒤의 경계값은 포함되지 않는다
# a <= x < b
print(a[1:-1]) 
print(a[1:9])
print(a[1:9:2])
url = 'http://uidesignguides.com/wp-content/uploads/2018/11/image.png'
# 위 문자열의 파일명 추출, 도메인 추출 등 데이터 정제에 사용 가능
print(a[:2], a[-2:]) # 앞에서 2개, 뒤에서 2개

# 멤버 함수(문자열)
a = '0123456789'
# 문자열 내 문자열 찾는 함수 : count vs index vs find
# 문자열 내에 특정 문자 개수
print('a 문자열 내 2의 개수 : ', a.count('2'))
print('a 문자열 내 A의 개수 : ', a.count('A')) # 없으면 0
# a라는 문자열에 "A"라는 문자가 존재하는가?
print(a.count('A') > 0) # False
print(a.index('2'))
# print(a.index('A')) # 에러 : 없는 문자는 예외처리 해야한다
print(a.find('2'))
print(a.find('A')) # 없으면 -1 반환
# => 문자열 내에서 문자열 찾기는 count(), find()를 사용해라

# 조인
b = ','
print(b.join(a)) # 0,1,2,3,4,5,6,7,8,9

# 분해
print(b.join(a).split(b)) # 리스트로 반환

# 공백 제거
a = '      abcdefg e df serwer       '
print('[%s]' % a.lstrip())
print('[%s]' % a.rstrip())
print('[%s]' % a.strip())
# 가운데 공백 제거 -> 정규식

# 대소문자
a = 'abcdABCD가나다라12341@#$'
print(a.upper())
print(a.lower())

# 조합 사용
url = 'http://uidesignguides.com/wp-content/uploads/2018/11/image.png'
# 파일명 image.png 추출
print(len(url.split('/')))
print(url.split('/')[len(url.split('/'))-1])
print(url.count('/'))
print(url.split('/')[url.count('/')])

# 포맷팅
a = 1
b = 2
# x + y = z 형식으로 출력
print('%d + %d = %d' %(a, b, a+b))
# %s로 받는 경우 => 데이터가 문자열일 때, 데이터의 타입을 모를 때
print('%s + %s = %s' %(a, b, a+b))
print('%d + %d = %f' %(a, b, a/b))
print('%d + %d = %s' %(a, b, a/b))
# .format() 처리
print('{} + {} = {}'.format(a, b, a+b))
print('{0} + {1} = {2}'.format(a, b, a+b))
print('{1} + {0} = {2}'.format(a, b, a+b))
# print('{1} + {1} = {1}'.format(a, b, a+b)) # format의 파라미터를 모두 다 쓸 필요는 없다.
print('{0} + {1} = {result}'.format(a, b, result = a+b)) # result는 지역변수

# 포맷팅, 자릿수 체크
print('[%s]' % '12345')
# 20칸에 배치
print('[%20s]' % '12345') # 오른쪽 정렬
print('[%-20s]' % '12345') # 왼쪽 정렬
print('[%0.2f]' % 3.1456789) # 반올림 -> 수치가 바뀐다
# print('[%0.2f]' % 3.1446789)
print('[%10.2f]' % 3.1456789)
# 치환식
a = 'abc{}efg'.format('K')
print(a)
# 자릿수 10개
a = 'abc{0:<10}efg'.format('K') # abcK         efg
print(a)
a = 'abc{0:>10}efg'.format('K') # abc         Kefg
print(a)
a = 'abc{0:^10}efg'.format('K') # abc    K     efg  / 짝수칸일 경우 앞쪽으로 센터 위치
print(a)
a = 'abc{0:*^10}efg'.format('K') # *로 빈칸 채우기
print(a)
