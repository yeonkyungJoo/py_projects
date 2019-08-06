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
obj = Person('컴퓨터', 1, 2)
print(obj)
obj.eat('피자')