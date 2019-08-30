[[ python web ]]

1. 웹 서비스 모듈
 > flask : 플라스크
  → 마이크로 에디션 → 필요한만큼 알아서 만든다 → nodejs → ex) jupyter
 > DJango : 장고
  → 풀스펙 에디션 → spring

2. python으로 웹을 구성하면 얻는 이득
 > 동일언어로 모든 시스템 구축
 > 호환은 기본, 이기종이라는 표현이 필요 없다

3. 단점
 > 리눅스에 서비스 구축시 조금 까다롭다
 > 페브릭이라는 모듈을 이용하여 자동화시킨다
   코드를 작성해서, 로컬PC에서 구동만 시키면 자동으로 서버 세팅 및 소스 업데이트까지 모두 완료
   + git를 같이 사용
 > flask는 nodejs와는 달리 단독으로 구동하면 안 된다(성능 때문에)
   apache or nginx 서버와 연동해서 사용

4. 설치
 $ pip install flask

5. flask 구조
 service
  └ public     : 정적 데이터, js, css, 이미지, 기타 등등
                 폴더명은 blueprint를 적용하면 변경 가능
  └ templates  : html 위치
  └ run.py 