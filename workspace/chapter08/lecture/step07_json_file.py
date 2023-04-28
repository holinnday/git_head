import json

user = {'id':1234, 'name': '홍길동'} #key와 value가 있는 python dict

print(type(user)) # dict
print(user['name']) #홍길동

#json 인코딩
jsonString = json.dumps(user, ensure_ascii=False)

#문자열 출력
print(jsonString)
print(type(jsonString))

#json 디코딩
pyObj = json.loads(jsonString)
print(type(pyObj))

# Dict 자료 확인
print(pyObj['name'])
for key in pyObj:
    print(key, ':', pyObj[key])


### jason 파일 디코딩 예시
# json file 읽기
file = open("D:/git_office/workspace/chapter08/data/usagov_bitly.txt", mode='r', encoding='utf-8')
lines = file.readlines()

#json 디코딩
rows = [ json.loads(row) for row in lines]
print('rows :', len(rows))

#10개 원소 출력
for row in rows[:10]:
    print(row)
    print(type(row))
file.close()

# dict -> data frame 변환
import pandas as pd
recode_df = pd.DataFrame(rows)
print(recode_df.info())