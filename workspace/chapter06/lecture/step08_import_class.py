lst = [1,3,5]
for i, c in enumerate(lst) :
    print('색인 : ', i, end=', ') #연속해서 콤마를 찍어라
    print('내용 : ', c)

dit = {'name' : '홍길동', 'job' : '회사원', 'addr' : '서울시'}
for i, k in enumerate(dit) :
    print('순서 : ', i, end=', ')
    print('키 :', k, end=', ')
    print('값 :', dit[k])

import datetime
from datetime import date, time

help(date)

today = date(2019, 10, 23)
print(today)

#date 객체 멤버변수 호출
print(today.year)
print(today.month)
print(today.day)

#date 객체 메서드 호출
w = today.weekday()
print('요일 정보 : ', w)

help(time)

currTime = time(21, 4, 30)
print(currTime)

print(currTime.hour)
print(currTime.minute)
print(currTime.second)

isoTime = currTime.isoformat()
print(isoTime)