# https://github.com/PyMySQL/PyMySQL
'''
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
'''

import pymysql

# 데이터베이스 접속은 I/O이므로 예외 상황이 항시 발생할 수 있다
# (예외처리) try ~
connection = None
try :
    # 1. 데이터베이스 접속 객체 생성(접속 정보 제공) → 접속
    connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = '12341234',
                                 db = 'python_db',
                                 charset = 'utf8mb4')
except Exception as e :
    print('오류 발생', e)

finally :
    # 2. 접속 닫기
    if connection : 
        connection.close()