# class
class Person :
    
    # 멤버 변수
    name = None
    age = 0
    weight = 0

    # 멤버 함수
    # self -> python, objective-c
    # - 클래스에서 멤버 함수의 1번 인자
    # - 파이썬에서 자기 자신 객체를 가르치는 키워드 
    # this -> java, js, 대다수 랭귀지

    def eat(self, food) :
        print('%s를 먹는다' % food)
    
    # 생성자 : 객체를 생성하고, 멤버 변수를 초기화하는 목적
    def __init__ (self, name, age, weight) :
        
        # 클래스 내부에서 멤버들에 접근할 때 : self.멤버(변수/함수)
        self.name = name
        self.age = age
        self.weight = weight

        # 부모 생성자 호출
        # return super().__init__()

    # 객체를 설명하는 코드를 구현하면 된다. 통상 문자열로 구성
    # 멤버 변수값이나 상태를 표현한 정보가 들어가면 OK
    # 자바의 toString()과 유사
    def __repr__ (self) :  
        return '''
        name = %s, age = %s, weight = %s
        ''' % (self.name, self.age, self.weight)

# 객체 생성
# obj = Person('컴퓨터', 1, 2)
# print(obj)
# obj.eat('피자')

# 상속
# 부모의 모든 것을 가지고, 재정의할 수 있고, 추가할 수 있다
class Xman(Person) :
    # 멤버 변수 추가
    abil = 100
    
    # 멤버 함수 추가
    def speed(self) :
        print('시속 500km로 달린다')
    
    # 재정의 (부모 대비 내용 구성이 달라진다) : 오버라이딩
    def eat(self, food) :
        print('%s를 1초만에 먹는다' % food)

    # 생성자도 확장
    def __init__(self, name, age, weight, abil) :
        # 부모 생성자를 이용한 멤버변수 초기화
        super().__init__(name, age, weight)
        self.abil = abil

# mu = Xman('파이썬', 200, 100, 103)
# mu.speed()
# mu.eat('피자')
# print(mu)
# print('p13_mod : __name__', __name__)

# 테스트 코드는 특정 조건을 만족할 때만 수행되게 구성
if __name__ == '__main__' :
    obj = Person('컴퓨터', 1, 2)
    print(obj)
    obj.eat('피자')

    mu = Xman('파이썬', 200, 100, 103)
    mu.speed()
    mu.eat('피자')
    print(mu)
    print('p13_mod : __name__', __name__)
