import json

file=open("D:/git_new/workspace/chapter10/data/labels.json", mode='r', encoding="utf-8")

lines = json.load(file)
print(type(lines))
print(len(lines))
print(type(lines[0]))

import pandas as pd
df = pd.DataFrame(lines)
print(df.info())
print(df.head())

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
    cursor =conn.cursor() # 실행 객체 생성

    # (4) table 생성
    sql = """create table labels(id int not null, url varchar(150) not null, name varchar(50) not null, color varchar(50) not null, de char(5))"""
    cursor.execute(sql) #table 생성

    # (5) 레코드 조회
    cursor.execute("select * from labels")
    rows = cursor.fetchall()

    if rows :   # (6) 레코드가 있는 경우 : 레코드 조회
        print("labels 레코드 조회")
        for row in rows :
            print(row)

        print("전체 레코드 수 : ", len(rows))
    else : #(7) 레코드 없는 경우
        for i in range(30) : # 30번 돌림
            uid = df.id[i]
            url = df.url[i]
            name = df.name[i]
            color = df.color[i]
            de = str(df.default[i])
            sql = f"insert into labels values({uid}, '{url}', '{name}', '{color}', '{de}')"
            cursor.execute(sql)
            conn.commit() # db 반영

except Exception as e:
    print('db error :', e)
finally:
    cursor.close()
    conn.close()

