
# coding: utf-8

# ## 데이터 획득
# 
# * api 사용
# * naver open api를 활용
# * urllib.request 모듈을 사용하여 통신처리 후 JSON 파싱을 통한 데이터 추출

# In[1]:


import os
import sys


# #### naver API 사용을 위한 키

# In[2]:


# https://developers.naver.com에서 Application 등록
Client_ID = 'Mv8PSDo4c0gpuASKyVoU'
Secret = 'Abej09hoFT'


# * 통신할 URL 정의
# * parameter 정의(get/post 방식에 맞춰 구성)
# * header 위에서 정의한 키 및 응답 데이터 포맷에 대한 구성 추가
# * 통신 -> 응답 코드 확인 -> 200번인 경우(성공) -> 응답데이터에서 json 데이터 획득
# * json 데이터에서 [가공 및 전처리는 일단 배제] 데이터 적재(csv or xls or database)

# In[3]:


# 네이버 통합 검색어 트렌드 조회 (https://developers.naver.com/docs/datalab/search/#python)
# 요청 url
url = "https://openapi.naver.com/v1/datalab/search"
url


# In[4]:


body = '{"startDate":"2019-07-09","endDate":"2019-08-06","timeUnit":"month","keywordGroups":[{"groupName":"대한민국","keywords":["대한민국","korean"]},{"groupName":"일본","keywords":["일본","japan"]}],"device":"pc","ages":["3","4"],"gender":"f"}';
body


# In[5]:


# 통신
import urllib.request as net


# In[6]:


# 통신 객체 생성
request = net.Request(url)  # request = urllib.request.Request(url)
# 헤더 설정
request.add_header("X-Naver-Client-Id", Client_ID)
request.add_header("X-Naver-Client-Secret", Secret)
request.add_header("Content-Type","application/json")


# In[7]:


request


# In[9]:


# 실제 통신 : post 방식
# 한글 데이터를 그대로 전송하면 오류 발생 -> body.encode('utf-8') 처리
# response = urllib.request.urlopen(request, data=body.encode("utf-8"))
response = net.urlopen(request, data=body.encode("utf-8"))


# In[11]:


response


# In[12]:


# 응답 코드가 정상이면
rescode = response.getcode()
if(rescode==200):
    # 실제 응답 데이터를 획득
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


# In[13]:


response_body


# In[14]:


response_body.decode('utf-8')


# In[20]:


import urllib


# In[15]:


# 뉴스 검색(https://developers.naver.com/docs/search/news/)
# 요청 url
news_url = 'https://openapi.naver.com/v1/search/news.json'


# In[21]:


# 파라미터
# query=%EC%A3%BC%EC%8B%9D&display=10&start=1&sort=sim HTTP/1.1

keyword = urllib.parse.quote('아베') # 검색어
news_param = 'query=%s&display=%s&start=%s&sort=%s' % (keyword, 10, 1, 'date')
news_param


# In[22]:


url = '%s?%s' % (news_url, news_param)
url


# In[23]:


# 통신 객체 생성
request = urllib.request.Request(url)
# 헤더 설정
request.add_header("X-Naver-Client-Id", Client_ID)
request.add_header("X-Naver-Client-Secret", Secret)


# In[24]:


request


# In[25]:


# 통신
response = urllib.request.urlopen(request)


# In[26]:


# 응답 코드가 정상이면
rescode = response.getcode()
if(rescode==200):
    # 실제 응답 데이터를 획득
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


# In[28]:


tmp = response_body.decode('utf-8')
tmp


# In[29]:


type(tmp)


# In[ ]:


# 원하는 데이터를 추출하려면 -> 파싱 -> xml, json 같은 형식을 취해야 한다


# In[30]:


# (다시 통신)
response = urllib.request.urlopen(request)


# In[31]:


import json


# In[32]:


# json에 로드
tmp = json.load(response)


# In[33]:


tmp


# In[34]:


type(tmp) # str -> dict


# In[ ]:


# json.parser.online.fr


# In[35]:


# 리스트는 for문으로 돌려서 데이터 획득
for item in tmp['items'] :
    print('-', item['title'])


# In[36]:


# 리스트 내포로 리스트화
[ item['title'] for item in tmp['items'] ]

