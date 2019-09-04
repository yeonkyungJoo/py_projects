# 머신러닝 모델을 기반으로 예측 함수를 구성
# 1. 모델 로드
from sklearn.externals import joblib
import os
import re
import json
# 서브 패키지라도, 패키지 경로는 무조건 엔트리 파일로부터 따져서 지정
from db import selectModelInfo

# 모든 경로는 entry 포인트를 기준으로 따진다

# 학습데이터 로드
# 예측 모델
info = selectModelInfo()
# 서버가 재가동될 때, 예측 모델을 로드하므로 
# 이 위치를 최신으로 갱신해준다
ml_model_file = info['dir'] # './ml/clf_lang_20190830.model'
clf = joblib.load(ml_model_file)

# 정답 로드
# 레이블
ml_label_file = info['label'] # './ml/clf_lang_labels.label'
with open ( ml_label_file, 'r' ) as f :
    clf_label = json.load(f)

# 판정 함수
def detect_lang(text) :
    # 데이터 벡터화
    text = text.lower()                 # 소문자로
    p = re.compile('[^a-zA-Z ]*')       # 영어를 제외한 불필요한 단어 제거용 정규식
    text = p.sub('', text)              # 정제 작업
    if not text.strip() :
        return None, None
    cnts = [ 0 for n in range(26) ]     # 벡터화된 데이터를 담을 리스트
    asc_a, asc_z, asc_ws = ord('a'), ord('z'), ord(' ') # 판단의 기준값 획득
    for ch in text :                    # 모든 글자 반복
        if ord(ch) != asc_ws :          # 아스키화, 알파벳이 맞으면
            cnts[ord(ch)-asc_a] += 1    # 빈도 증가
    total_cnt = sum(cnts)               # 전체 빈도 계산
    if total_cnt == 0 :                 # 빈도가 없다 → 영어 아님 → 판독 불가
        return None, None        
    freq = list( map( lambda x : x/total_cnt, cnts ))   #   정규화

    # 정답 로드 (매번 할 필요가 없으므로 위로)

    # 예측 판정, 리턴
    res = clf.predict( [freq] )         # 타입을 맞춰주기 위해 []
    if res :
        return res[0], clf_label[res[0]]
    else :
        return None, None


