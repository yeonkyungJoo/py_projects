# 조건문, 반복문
# 내장함수 input() : Terminal을 통해 사용자 입력을 받는다
# 문자열을 리턴, 인자를 넣으면 프롬프트로 사용된다

price = int(input('막국수는 얼마인가요? ')) 
print(price) # 입력 전까지는 실행 X, 전형적인 동기식 프로그램

# :(콜론) : 조건문, 반복문 등 문장의 끝을 의미하고, 코드블럭을 시작하라는 의미
if price > 6000 :
    # pass : statement 최소 1줄에 대한 조건만족, 아무것도 하지 마라
    print('비싸다')
    pass
elif price == 6000 :
    print('적절하다')
    pass
else :
    print('싸다')
    pass