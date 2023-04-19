import os
print('\n현재 경로', os.getcwd())

#예외처리 (파일이 있는지 없는지 여부를 체크)
try :
    #파일 읽기
    ftest1 = open('chapter08/data/ftest.txt', mode = 'r')
    print(ftest1.read()) #파일 전체 읽기
    #파일 쓰기
    ftest2 = open('chapter08/data/ftest2.txt', mode = 'w')
    ftest2.write('my first text~~~')
    #파일 쓰기 + 내용 추가
    ftest3 = open('chapter08/data/ftest2.txt', mode = 'a')
    ftest3.write('\nmy second text ~~~') #파일 쓰기 추가

except Exception as e:
    print('Error 발생 : ', e)

finally :
    ftest1.close() #파일 객체 닫기
    ftest2.close()
    ftest3.close()

# 파일 읽기 관련 함수

try :
    ftest = open('chapter08/data/ftest.txt', mode = 'r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    ftest = open('chapter08/data/ftest.txt', mode='r')
    lines = ftest.readlines()
    print(lines)
    print(type(lines))
    print('문단수 :', len(lines))

    docs = [] #리스트 형식으로 문장 선언
    for line in lines:
        print(line.strip()) #text만 출력
        docs.append(line.strip())

    ftest = open('chapter08/data/ftest.txt', mode='r')
    line = ftest.readline()
    print(line)
    print(type(line))

except Exception as e:
    print('Error 발생 : ', e)

finally :
    ftest.close() #파일 객체 닫기


