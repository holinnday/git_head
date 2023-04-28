import pandas as pd
import os
print(os.getcwd())

#csv 파일 읽기
score = pd.read_csv("D:\git_office\workspace\chapter08\data/score.csv")
print(score.info())
print(score.head())

# 칼럼 추출
kor = score['kor']
eng = score['eng']
mat = score['mat']
dept = score['dept']

#과목별 최고 점수 (상위 함수 그대로 씀)
print('max kor = ', max(kor))
print('max eng = ', max(eng))
print('max mat = ', max(mat))

#과목별 최하 점수
print('min kor = ', min(kor))
print('min eng = ', min(eng))
print('min mat = ', min(mat))

#과목별 평균 점수
from statistics import mean
print('국어 점수 평균 : ', round(mean(kor), 3)) #round를 써서 반올림해 소수점 세자리까지 표현, 네번째 자리에서 반올림함. round(값, 소수점 숫자)
print('영어 점수 평균 : ', round(mean(eng), 3))
print('수학 점수 평균 : ', round(mean(mat), 3))

# dept 빈도수
dept_count = {}

for key in dept :
    dept_count[key] = dept_count.get(key, 0) + 1

print(dept_count)

sam = pd.ExcelFile("D:/git_office/workspace/chapter08/data/sam_kospi.xlsx")

#excel 피싱
kospi = sam.parse("sam_kospi")
print(kospi.info())

#칼럼 추출
high = kospi['High']
low = kospi['Low']

#평균 계산
from statistics import mean
print('High mean=', mean(high))
print('low mean=', mean(low))

#평균 계산
print('High mean=', high.mean())
print('Low mean=', low.mean())