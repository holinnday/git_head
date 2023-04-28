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
    conn = pymysql.connect(**config)
    cursor =conn.cursor()

    while True : # 무한 루프
        print('\t[레코드 처리 메뉴]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 레코드 종료')
        menu = int(input('\t메뉴번호 입력 : '))

        if menu == 1 :
            sql = "select * from goods"
            cursor.execute(sql)
            datatable = cursor.fetchall()

            for row in datatable :
                print(f"{row[0]} {row[1]} {row[2]}  {row[3]}")
            print('전체 레코드 수 : ', len(datatable))

        elif menu == 2 :
            code = int(input(' 추가할 상품 코드 : '))
            name = input('추가할 상품명 : ')
            su = int(input('추가할 수량 : '))
            dan = int(input('추가할 단가 : '))

            sql = f"insert into goods values({code}, '{name}', {su}, {dan}) "
            cursor.execute(sql)
            conn.commit()

        elif menu == 3 :
            code = int(input('수정할 상품 코드 : '))
            su = int(input('수정할 수량 : '))
            dan = int(input('수정할 단가 : '))

            sql = f"update goods set su = {su}, dan = {dan} where code = {code}"
            cursor.execute(sql)
            conn.commit()

        elif menu == 4 :
            code = int(input('삭제할 상품 코드 : '))
            sql = f"select * from goods where code = {code}"
            cursor.execute(sql)
            rows = cursor.fetchall()

            if rows:
                print('레코드 삭제')
                sql = f"delete from goods where code = {code}"
                cursor.execute(sql)
                conn.commit()
            else:
                print('해당 코드 없음')

        elif menu == 5 :
            print('프로그램 종료')
            break # 반복 종료
        else :
            print('해당 메뉴는 없습니다.')

# DB 연결 예외 처리
except  Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()