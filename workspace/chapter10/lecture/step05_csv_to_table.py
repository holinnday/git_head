import pandas as pd
import pymysql
bmi = pd.read_csv("D:/git_new/workspace/chapter10/data/bmi.csv")
print(bmi.info())
# (2) 각 칼럼 추출
height = bmi['height']
weight = bmi['weight']
label = bmi['label']
# 환경 변수
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
    cursor =conn.cursor() # 실행 객체 생성
    # (3) table 조희
    cursor.execute("show tables")
    tables = cursor.fetchall()

    # (4) 스위칭기법
    sw = False
    for table in tables :
        if table[0] == 'bmi_tab' : # bmi_tab을 만들기 위함. 테이블이 있는 경우 true, 테이블이 없는 경우 그대로 false.
            sw = True

    # (5) 테이블 생성
    if not sw : # not sw(false) == true
        print('테이블 없음')
        sql = """create table bmi_tab(height int not null, weight int not null, label varchar(15) not null)"""
        cursor.execute(sql)
    # (6) 레코드 조회
    cursor.execute("select * from bmi_tab")
    rows = cursor.fetchall()

    if rows :   # (7) 레코드가 있는 경우 : 레코드 조회
        for row in rows :
            print(f"{row[0]}    {row[1]}    {row[2]}")
        print('전체 레코드 수 : ', len(rows))
    else: #(8) 레코드 없는 경우 : 레코드 추가
        print("100 레코드 추가")
        for i in range(100) : # 백번 돌림
            h = height[i]
            w = weight[i]
            lab = label[i]
            cursor.execute(f"insert into bmi_tab values({h}, {w}, '{lab}')")
            conn.commit()

except Exception as e:
    print('db error :', e)
finally:
    cursor.close()
    conn.close()
