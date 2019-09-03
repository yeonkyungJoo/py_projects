# 엔트리 포인트 → 여기서부터 경로를 따진다
# 1. 모듈 가져오기
from flask import Flask, render_template, request, jsonify, redirect
from ml import detect_lang
import os
import sys
import urllib.request
import json
from db import insertData

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
@app.route('/devgo', methods=['GET', 'POST'])
def devgo() :
    if request.method == 'GET' :
        # 기본으로 templates 폴더 밑에서 찾는다
        return render_template('index.html')
    else :
        # post방식으로 요청되었을 때 처리
        # (서버) 데이터를 획득 → 벡터화 → 모델을 로드(서버 가동 시 1회만) → 예측 → 답안 획득 → 응답 구성
        # 1. 데이터 획득 (딕셔너리로)
        # check_text = request.form['inputLang']
        check_text = request.form.get('inputLang')  # 위 방식보다 더 선호 : 키가 틀려도 None으로 처리
        nation, lang_ko = detect_lang( check_text ) # 판정

        # 1. 번역 요청 → 파파고 번역과 연동(통신)
        transText = lang_transByPapago( check_text, nation )
        '''
        [응답 형식]
        {
            "message": {
                "@type": "response",
                "@service": "naverservice.nmt.proxy",
                "@version": "1.0.0",
                "result": {
                    "srcLangType":"ko",
                    "tarLangType":"en",
                    "translatedText": "tea"
                }
            }
        }   
        '''
        if transText :      # 번역 성공 시
            transText = transText['message']['result']['translatedText']
        else :
            transText = '번역 실패'

        # 2. 로그 처리(DB 저장)
        insertData( src = check_text, out = transText, slang = nation, olang = 'ko' )
        return jsonify( { 'code' : nation, 'ko' : lang_ko, 'trans' : transText } )

# 파파고 번역 연동
Client_ID = 'Mv8PSDo4c0gpuASKyVoU'
Client_Secret = 'Abej09hoFT'
'''
curl "https://openapi.naver.com/v1/papago/n2mt" \
-H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
-H "X-Naver-Client-Id: Mv8PSDo4c0gpuASKyVoU" \
-H "X-Naver-Client-Secret: Abej09hoFT" \
-d "source=ko&target=en&text=만나서 반갑습니다." -v
'''
# https://developers.naver.com/docs/nmt/examples/#python
def lang_transByPapago( text, na_code = 'en' ) :
    # 사용자 인증 키
    client_id = Client_ID
    client_secret = Client_Secret

    # 전송할 데이터(번역 요청 원문) URL 인코딩 처리(목적 : 한글 깨짐 방지)
    encText = urllib.parse.quote(text)

    # 통신 준비
    data = "source={0}&target=ko&text={1}".format( na_code, encText )
    url = "https://openapi.naver.com/v1/papago/n2mt"

    # 요청 객체 생성
    request = urllib.request.Request(url)
    # 헤더 설정
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    # 요청
    response = urllib.request.urlopen(request, data = data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200) :
        # 통신 성공 → 응답 데이터를 json.load를 통해 파이썬의 객체로 리턴
        return json.load(response)
        # response_body = response.read()
        # print(response_body.decode('utf-8'))
    else :
        # 통신 실패
        return {}
        # print("Error Code:" + rescode)
    

# 4. 서버 가동
if __name__ == '__main__' : # 조건문 이하 코드는 run.py가 직접 구동될 때만 작동
    app.run( debug = True )