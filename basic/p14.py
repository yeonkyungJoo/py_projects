# 모듈화 + 패키지
# > 모듈 만들기, 테스트 코드 배치, 모듈 가져오기, 패키지 사용

# 모듈 : *.py
#       ex) (내가 만든) mod.py, __init__.py, p1.py, p2.py, ...
# 모듈화의 대상 : 변수, 함수, 클래스 -> 이 요소들을 가져다가 내 것처럼 사용 가능
#                ex) (내가 만든) PI, PI2, PI3, add() 등
# 패키지 -> 유사한 기능끼리 묶어둔 디렉토리, 유틸리티, 통신, gui 등등 모아둔 것
#           a, b 폴더
#           패키지 폴더 내에 __init__.py 이 파일은 하위 호환을 위해서 python 3.3 이하에서는 모두 사용한다.
#           그리고 __init__.py는 곧 해당 패키지 자체를 의미한다.

# from (출처)패키지.패키지...모듈 import 변수/함수/클래스 (필요한 것들 열거)
from a.b.mod import PI, add
print(PI)
print(add(1, 2))

# from 패키지.패키지 import 변수/함수/클래스 (필요한 것들 열거)
# 경로상 마지막 패키지(디렉토리) 안에 있는 __init__.py에서 모듈을 가져온다.
from a.b import PI2
print(PI2)

# -> 패키지명은 절대로 . 들어가면 안 된다.
# -> 모듈명도 절대로 . 들어가면 안 된다.
# 왜? 경로명으로 인식할 수 있기 때문

from a import PI3
print(PI3)

# 별칭 : 이름이 너무 길어서 혹은 이름을 변경해서 사용하고 싶다면
# 원래이름 as 별칭
from a import PI3 as pi
print(pi) # 이제 PI3는 사용할 수 없다.

# 가져올 모듈이 너무 많다. 다 가져왔으면 좋겠다 => *
# 하위 호환을 위해서는
# __all__=['mod']
from a.b import *
print(mod.PI, PI2)

# import만 사용 시
# as로 별칭을 쓴다
import a.b.mod as m
print(m.PI)

import a.b as bm
print(bm.PI2)

# 모듈을 가져온다는 것은 해당 모듈을 실행한다고 봐도 무방 -> 메모리 적재를 해야하기 때문
# 내가 만든 모듈같은 경우 의도하지 않은 코드가 실행될 수 있다.
# -> 테스트하려고 만든 코드는 모듈 가져오기 수행 시 실제로 구동되면 안 된다.
# -> 이런 코드 처리가 필요하다 -> __name__을 이용하여 처리한다

# __name__을 사용하는 모듈을 직접 구동하면 "__main__"으로 나오고
# 모듈로 사용되면(즉, 다른 모듈이 가져다 쓰면) "모듈명"으로 나온다.

from p13_mod import Xman
mu = Xman('마동석', 100, 50, 52)
print(mu)
                                  # p13_mod : __name__ p13_mod
print('p14 : __name__', __name__) # p14 : __name__ __main__


# p13_mod.py 참고