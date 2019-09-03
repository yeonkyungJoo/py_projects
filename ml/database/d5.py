# 함수화
import pymysql

# uid의 데이터를 가져오는 함수
def selectData(uid) :
    connection  = None
    result = None       # []도 가능
    try :
        connection = pymysql.connect(host = 'localhost',
                                     user = 'root',
                                     password = '12341234',
                                     db = 'python_db',
                                     charset = 'utf8mb4',
                                     cursorclass = pymysql.cursors.DictCursor)
        with connection.cursor() as cursor :
            sql = '''
            select src, slang as label from tbl_trans_log where uid = %s;
            '''
            cursor.execute(sql, ( 'guest', ))
            result = cursor.fetchall()
            # print(result)
    except Exception as e :
        print('오류 발생', e)
    finally :
        if connection :
            connection.close()
    return result

# 번역을 요청한 데이터를 DB에 삽입하는 함수
def insertData( src, out, slang, olang, uid = 'guest' ) :
    connection = None
    result = 0
    try :
        connection = pymysql.connect(host = 'localhost',
                                     user = 'root',
                                     password = '12341234',
                                     db = 'python_db',
                                     charset = 'utf8mb4',
                                     cursorclass = pymysql.cursors.DictCursor)
        with connection.cursor() as cursor :
            sql = '''
            INSERT INTO `tbl_trans_log` 
            (`src`, `out`, `slang`, `olang`, `uid`)
            VALUES
            (%s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (src, out, slang, olang, uid))
        # 데이터베이스에 실제 반영
        connection.commit()
        # 영향을 받은 row 수
        result = connection.affected_rows()
    except Exception as e :
        print('오류 발생', e)
    finally :
        if connection :
            connection.close()
    return result

# 테스트 코드
if __name__ == '__main__' :     # 모듈 import 시 수행되지 않도록
    print('→', selectData('guest'))
    print('→', insertData('Hello', '안녕하세요', 'en', 'ko'))
