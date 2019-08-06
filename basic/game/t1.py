# 문자열을 숫자(정수)로 변환이 가능한지 체크하는 내용
a = [
    '',
    '1',
    '1.1',
    'A',
    'a',
    '@',
    '가'
]

for i in a :
    print(i, i.isalpha(), i.isdigit(), i.isnumeric())