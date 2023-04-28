import pandas as pd
import os
#file 읽기
emp = pd.read_csv('D:/git_office/workspace/chapter08/data/emp.csv', encoding='utf-8')
print(emp.info())


name = emp['Name']
pay = emp['Pay']

print("관측지 길이 : ", len(emp))

from statistics import mean
print("전체 평균 급여 : ", mean(pay))

low = min(pay)
high = max(pay)

for idx in range(len(pay)) :
    if pay[idx] == low :
        print('최저 급여: %d, 이름 : %s' % (low, name[idx]))
    if pay[idx] == high :
        print('최고 급여: %d, 이름 : %s' % (high, name[idx]))
