'''
연속데이터(시퀀스 타입)
    > 딕셔너리 : {} -> 순서 x, key:value 구조
                      키는 중복되면 X, 값 중복 OK
                   => 테이블 상의 한 개의 row, json의 객체, js 객체와 동일
'''

dic = {}
print(dic, len(dic), type(dic)) # {} 0 <class 'dict'>
dic = dict()
print(dic, len(dic), type(dic)) # {} 0 <class 'dict'>

# 키를 통해서 값을 이해할 수 있다. 직관적으로
dic = {
    'name' : '홍길동',
    'age' : 100
}
print(dic, len(dic), type(dic)) # {'name': '홍길동', 'age': 100} 2 <class 'dict'>

# 인덱싱 : 순서가 없으므로, 데이터를 특정할 수 있는 키 값을 사용한다
print(dic['name']) # 홍길동

# 데이터 추가, 키는 뭐든지 올 수 있다
dic[2] = 'hello'  # 2는 인덱스가 아닌, 키를 의미
print(dic, len(dic), type(dic)) # {'name': '홍길동', 'age': 100, 2: 'hello'} 3 <class 'dict'>


print(dic.keys()) # dict_keys(['name', 'age', 2])
print(dic.values()) # dict_values(['홍길동', 100, 'hello'])
# -> output이 리스트이므로 순서가 중요

# 키 조사
print('name' in dic) 