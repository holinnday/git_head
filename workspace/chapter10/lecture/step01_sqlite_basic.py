import sqlite3
print(sqlite3.sqlite_version_info)

try :
    # db 연동 객체 생성
    conn = sqlite3.connect("D:/git_office/workspace/chapter10/data/sqlite_db") #db가 새로 생성되고 conn 객체로 연결됨
    # sql 실행 객체
    cursor = conn.cursor()

    # table 생성
    sql = 'create table if not exists test_table(name text(10), phone text(15), addr text(50))'
    cursor.execute(sql) # sql문 실행 (실행 객체를 가지고 sql 을 실행해야됨) test_table을 생성함

    #레코드 추가 (만들어둔 테이블에 자료를 추가하는 과정)
    cursor.execute("insert into test_table values('홍길동', '010-1111-1111', '서울시')")
    cursor.execute("insert into test_table values('이순신', '010-2222-2222', '해남시')")
    cursor.execute("insert into test_table values('강감찬', '010-1111-1111', '평양시')")
    conn.commit()  #데이터베이스 연동 객체를 이용해 commit 함수를 호출해 db에 반영

    #레코드 조희
    cursor.execute("select * from test_table")
    rows = cursor.fetchall() # cursor 객체를 이용하여 fetchall() 함수를 호출해 조회된 전체 레코드를 가져옴

    #레코드 출력
    for row in rows : #전체 레코드를 저장한 rows를 for 문으로 반복하여 한 줄의 레코드 단위로 출력
        print(row)

    print('이름 \t 전화번호    \t주소')
    for row in rows :
        print(row[0], '\t', row[1], '\t', row[2] )

except Exception as e :
    print('db 연동 실패 : ', e)
    conn.rollback() #실행 취소 (전부 환원)

finally:
    cursor.close() # cursor 객체 닫기
    conn.close() # conn 객체 닫기


