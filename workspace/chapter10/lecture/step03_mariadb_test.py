import pymysql
# db 연동 환경변수
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True}

try : #db 연동시 예외가 발생할 수 있기 때문에 try 문을 이용함
    conn = pymysql.connect(**config) # (3) dict(KEY와 VALUE)를 받을때는 ** 사용하여 db 연동 객체 생성
    cursor = conn.cursor() # (4) sql문 실행 객체
    # (5) 테이블 조회
    sql = "show tables"
    cursor.execute(sql)
    tables = cursor.fetchall() #검색된 테이블 목록 가져오기
    # (6) 전체 table 목록 출력
    print(tables)  # (('goods',),) : work 데이터베이스 안의 goods 테이블

    # (7) table 유무 확인
    if tables: # 한개 이상의 레코드가 있기 때문에 있음으로 출력됨
        print('table 있음')
    else:
        print('table 없음')

except Exception as e :
    print('db error : ', e)

finally:
    cursor.close()
    conn.close()