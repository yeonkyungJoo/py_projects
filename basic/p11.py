# 함수
# function, method
# 반복작업 해소, 재활용성 높이고, 구조적 설계 -> 개발시간 단축

'''
def 함수명( [인자명, 인자명, ...] ) :
    statement
    [ return 값 ]
'''

# 함수 정의
def add(x, y) :
    return x+y

# 함수 사용
d = add(1, 2)
print(d)

# 가변인자, 함수의 입력의 수가 가변
def add2(*args) :
    # print(args)
    # 인자로 전달된 데이터를 모두 더해서(누적합) 리턴하시오
    result = 0
    for i in args :
        result += i
    return result

print(add2(1, 2))
print(add2(1, 2, 3))

# 가변인자로 전달된 데이터의 누적합, 누적곱을 계산하여 리턴하시오
def mix(*args) :
    sum , mul = (0, 1)
    for i in args :
        sum += i
        mul *= i
    return sum, mul    # 리턴할 값이 여러 개면 튜플로 return
print(mix(1, 2, 3, 4))

# 값을 각각 받고 싶은 경우 
a, b = mix(1, 2, 3, 4) # 데이터를 받을 때 반드시 순서를 확인해야 한다
print(a)
print(b)

# 리턴을 딕셔너리로 해보자 : 출력 결과에 대해서 순서를 몰라도 된다. 키만 알면 된다
def mix2(*args) :
    sum, mul = (0, 1)
    for i in args :
        sum += i
        mul *= i
    return { 'sum' : sum, 'mul' : mul }

print( mix2(1, 2, 3, 4, 5, 6)['sum'])
print( mix2(1, 2, 3, 4, 5, 6)['mul'])

# 로그함수
env_debug = True
def log(msg) :
    if env_debug :
        print('-'*40)
        print(msg)
        print('-'*40)
log('이것은 로그 메세지 출력 함수입니다.')

# 내장함수 : len(), type(), int(), str(), tuple(), dict(), list() 등
# 외장함수 :random.randint(), sys.exit() 

# 사용자 정의 함수 : 형태를 정의할 수 없다. 만드는 사람 마음이니까 
#                   -> 프로젝트 시 네이밍에 대한 정의가 필요하다

# 함수 인자의 초기값 주기
# def setPerson(name='컴퓨터', age=10, weight=50, score) :   // error
#   -> 초기화 안 해준 인자가 앞으로 와야 한다
def setPerson(score, name='컴퓨터', age=10, weight=50) :
    log('%s %s %s %s' % (name, age, weight, score))

setPerson(100)
setPerson(score=30)
# setPerson(name = '모라')      // error
#   -> 기본값이 없는 함수의 파라미터는 반드시 값을 부여해야 한다

# 그냥 나열하면 순서대로 인자가 전달된다
setPerson(1, 2, 3, 4)   # 2 3 4 1

# 기본값이 부여된 파라미터들은 함수 호출 시 순서에 상관없이 명시적으로 사용 가능
setPerson(1, age=1004, name='모라')

log(msg='가나다라')     # 파라미터 1개짜리 함수도 명시적으로 인자 전달 가능
log('가나다라')

