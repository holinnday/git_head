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
    cursor = conn.cursor()

    cursor.execute(f"select * from bmi_tab where height >= 170 and height <=180")


    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]}    {row[1]}    {row[2]}")
    print('전체 레코드 수 :', len(rows))
     # 조건 2 : label 입력
    label = input("검색할 label 입력 : ")
    sql = f"select * from bmi_tab where label like '%{label}%' "
    cursor.execute(sql)
    rows = cursor.fetchall()
    if rows:
        for r in rows:
            print(r[0], r[1], r[2])
        print('해당 label의 레코드 수 :', len(rows))
    else:
        print('해당 label 없음')

except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
