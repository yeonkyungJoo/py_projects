[[ 자연어 처리 ]]
1. 개요
 - 한글 자연어 처리를 파이썬으로 수행하는 과정
 - 모듈명 : KoNLPy(코엔엘파이)
  1) https://konlpy-ko.readthedocs.io/ko/v0.4.3/
  2) 파이썬의 간결함, 우아하고 강력한 스트링 연산 기능을 최대한 살림
  3) 여러 형태소 분석기들이 포함 : 꼬꼬마, 한나눔, MeCab-Ko 등등
  4) 자연어 처리에 필요한 각종 사전, 말뭉치, 도구, 튜토리얼 제공
  5) 쉽다

2. 설치 과정(anaconda의 base 환경에서 설치)
 - 반드시 순서대로 할 것
 
 - KoNLPy 설치
   $ pip install konlpy
 
 - jdk 설치
   $ java -version (자바 버전 확인)
 
 - 환경변수 추가
   > 윈도우 : JAVA_HOME = jdk 경로 설정
     내 PC > 우클릭 > 속성 > 고급 시스템 설정 > 환경변수 >
     User에 대한 사용자 변수 새로 만들기 >
         - 변수 이름 : JAVA_HOME
         - 변수 값 : C:\Program Files\Java\jre1.8.0_211
   > 맥 : export JAVA_HOME = $('/usr/libexec/java_home)
 
 - python으로 자바 라이브러리를 사용하는 모듈 설치
   > 자신이 Java라고 생각하고 Java 라이브러리를 설치할 수 있는 모듈
   > conda install -c conda-forge jpype1
     간혹 운영체제의 버전, JDK의 버전, jupyter 경로 상에, 혹은 PC 이름이 한글이면 안 될 수도 있다.

 - python용 라이브러리 nltk 설치
   > base 가상환경은 nltk가 설치되어 있다
   $ python
   > import nltk
   > nltk.download()
   
 - Raw text용 워드클라우드, 젠심
   $ pip install wordcloud gensim
      
3. KoNLPy 형태소 분석기
 
 - Hannanum
   > 1999년부터 KAIST 시맨틱웹 연구센터(SWRC)에서 개발(자바)
 - Kkma
   > SNU의 지능형 데이터 시스템(IDS)연구소에서 개발 -> 자바로 개발, 형태소 분석, 자연어 처리 시스템
 - Mecab
   > 일본의 형태소 분석기와 교토 대학 정보학과 연구소에서 개발한 POS tagger을 Mecab-ko로 변경하여 한국어에 적용
 - Okt(트위터)
   > Will Hohyon Ryu, 개발한 scala로 연구개발, 한국어 토크나이저
 - Komoran
   > 2013년도, Shinware에서 개발, 자바로 작성된 새로운 오픈소스 한국어 형태학 분석기


4. 형태소 분석기별 함수들의 의미

5. pos 함수에 대한 형태소별 의미