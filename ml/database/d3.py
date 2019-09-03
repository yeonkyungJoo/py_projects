import pymysql

connection = None
try :
    connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = '12341234',
                                 db = 'python_db',
                                 charset = 'utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor)
    # with connection.cursor(cursor = pymysql.cursors.DictCursor) as cursor :                            
    # 위 방법은
    # 매번 커서를 획득할 때마다 타입을 지정하는 방식(→비효율), 각기 다르게 적용할 때 가능
    with connection.cursor() as cursor :
        sql = '''
        select src, slang as label from tbl_trans_log;
        '''
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
except Exception as e :
    print('오류 발생', e)
finally :
    if connection :
        connection.close()                             