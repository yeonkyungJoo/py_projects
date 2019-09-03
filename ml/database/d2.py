import pymysql

connection = None
try :
    # 1. 데이터베이스 접속 객체 생성(접속 정보 제공) → 접속
    connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = '12341234',
                                 db = 'python_db',
                                 charset = 'utf8mb4')
    
    # 2. 커서를 획득한다
    # cursor = connection.cursor() ~ cursor.close()
    with connection.cursor() as cursor : 
        # 3. 쿼리를 수행한다
        sql = '''
        select src, slang as label from tbl_trans_log;
        '''
        # 쿼리 수행 시 데이터를 넣고 싶다면 튜플로 2번 인자에 채운다
        cursor.execute(sql)
        # 4. 결과 획득(select) 혹은 커밋(insert, update, delete)
        # fetchall() : 다 가져온다 / fetchone() : 한 개만 가져온다
        result = cursor.fetchall()
        print(result)
        # 구조가 튜플 내 튜플 형태로 나온다 ( (), (), () )
        # 리스트 형태가 제일 적합할 것
        # => 접속 객체 생성 시, cursorclass=pymysql.cursors.DictCursor
except Exception as e :
    print('오류 발생', e)
finally :
    # 3. 접속 닫기
    if connection :
        connection.close()