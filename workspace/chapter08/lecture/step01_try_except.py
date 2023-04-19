print('프로그램 시작 !!!')

x = [10, 30, 25.2, 'num', 14, 51]

for i in x :
    print(i)
    y = i**2
    print('y =', y)

print('프로그램 종료')

# 예외 처리 코드 (try)
print('프로그램 시작 !!!')

x = [10, 30, 25.2, 'num', 14, 51]

for i in x :
    try :
        y = i**2
        print('i= ', i, 'y=', y)
    except :
        print('숫자 아님 :', i)

print('프로그램 종료')

#유형별 예외처리
print('\n유형별 예외처리')
try :
    div = 1000 / 2.53
    print('div = %5.2f' %(div))
    div = 1000 / 0
    f = open('c:\\text.txt')
    num = int(input('숫자입력 : '))
    print('num =', num)

#다중 예외처리 클래스
except ZeroDivisionError as e:
    print('오류 정보 :', e)
except FileNotFoundError as e:
    print('오류 정보 :', e)
except Exception as e:
    print('오류 정보 :', e)

finally :
    print('finally 영역 - 항상 실행되는 영역')