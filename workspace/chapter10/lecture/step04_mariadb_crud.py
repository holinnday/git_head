import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True}

try :
    conn = pymysql.connect(**config) # (3) dict(KEY와 VALUE)를 받을때는 ** 사용하여 db 연동 객체 생성
    cursor = conn.cursor() # (4) sql문 실행 객체
    '''
    # (1) table 생성
    sql = """create table goods(code int primary key, name varchar(30) not null, su int default 0, dan int default 0)"""
    cursor.execute(sql)
    '''
    # (2) 레코드 추가
    code = int(input('코드 입력 : '))
    name = input('상품명 입력 : ')
    su = int(input('수량 입력 : '))
    dan = int(input('단가 입력 : '))

    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)  # 레코드 추가
    conn.commit() # db 반영

    # (3) 전체 목록 보기
    sql = "select * from goods"
    cursor.execute(sql)
    rows = cursor.fetchall()

    # 레코드 출력:  양식 문자
    for r in rows :
        print('%d   %s  %d  %d'%r)

    print('검색 레코드 수 : ', len(rows))

    # (4) 상품명 조회
    name = input('\n조회할 상품명 입력 : ')
    sql = f"select * from goods where name like '%{name}%'"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows :
        for r in rows :
            print(r[0], r[1], r[2], r[3])

    else:
        print('해당 상품 없음')

except Exception as e :
    print('db 연동 오류 :', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()

