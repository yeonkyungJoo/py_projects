# 엔트리 포인트 → 여기서부터 경로를 따진다
# 1. 모듈 가져오기
from flask import Flask, render_template, request, jsonify, redirect
from ml import detect_lang

# 2. flask 객체 생성
app = Flask(__name__)

# 3. 라우팅
# ~/ 요청하면 home()이 응답(return)
@app.route('/')
def home() :
    # return '<b>helloworld</b>
    return redirect('/devgo')

# restful api
# 기본 라우트는 get방식만 허용
@app.route('/', methods=['GET', 'POST'])
def devgo() :
    if request.method == 'GET' :
        # 기본으로 templates 폴더 밑에서 찾는다
        return render_template('index.html')
    else :
        # post방식으로 요청되었을 때 처리
        # (서버) 데이터를 획득 → 벡터화 → 모델을 로드(서버 가동 시 1회만) → 답안 획득 → 응답 구성
        # 1. 데이터 획득 (딕셔너리로)
        # check_text = request.form['inputLang']
        check_text = request.form.get('inputLang')  # 위 방식보다 더 선호 : 키가 틀려도 None으로 처리
        nation, lang_ko = detect_lang( check_text ) # 판정
        return jsonify( { 'code' : nation, 'ko' : lang_ko } )

# 4. 서버 가동
if __name__ == '__main__' : # 조건문 이하 코드는 run.py가 직접 구동될 때만 작동
    app.run( debug = True )