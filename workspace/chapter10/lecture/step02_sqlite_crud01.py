import sqlite3

try :
    conn = sqlite3.connect("D:/git_office/workspace/chapter10/data/sqlite_db")  # db가 새로 생성되고 object(conn)로 연결됨
    cursor = conn.cursor()  # sql 실행 객체 생성

    sql = """create table if not exists goods(code integer primary key, name text(30) unique not null, su integer default 0, dan real default 0.0)"""
    cursor.execute(sql)

    '''
    cursor.execute("insert into goods values(1, '냉장고', 2, 8500000)") #모두 입력할때는 칼럼명 생략가능. 다 써줘도 됨.
    cursor.execute("insert into goods values(2, '세탁기', 3, 5500000)")
    cursor.execute("insert into goods(code, name) values(3, '전자레인지')") #일부 칼럼만 넣을경우 칼럼 이름을 정의해줘야함
    cursor.execute("insert into goods(code, name, dan) values(4, 'HDTV', 15000000)")
    conn.commit() #db 반영
    '''
    # (5) 레코드 추가: 2차
    code = int(input('code 입력 : '))
    name = input('name 입력 : ')
    su = int(input('su 입력 : '))
    dan = int(input('dan 입력 : '))

    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql) #레코드 추가
    conn.commit()

    # 레코드 수정
    code = int(input('수정 code 입력 : '))
    su = int(input('수정 su 입력 : '))
    dan = int(input('수정 dan 입력 : '))

    sql = f"update goods set su = {su}, dam = {dan} where code = {code}"
    cursor.execute(sql)  # 레코드 추가
    conn.commit()

    # 레코드 조회
    sql = "select * from goods" #where 문이 없는것은 다 읽어오라는 의미(모든 칼럼)
    cursor.execute(sql)
    rows = cursor.fetchall() #레코드 가져오기

    for row in rows :
        print(row[0], row[1], row[2], row[3]) # 하나씩 출력
        print('검색된 레코드 수 : ', len(rows))
        # 상품명 조회
        name = input("상품명 입력 : ")
        sql = f"select * from goods where name like '%{name}%'" #f string %{name}% name의 앞뒤로 뭐가 있던 상관없이 불러와라
        cursor.execute(sql)
        rows = cursor.fetchall()

        if rows : # rows에 무언가 있다면
            for row in rows :
                print(row)
        else :
            print('검색된 레코드 없음')


except Exception as e :
    print('db 연동 error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()

'''
    




'''