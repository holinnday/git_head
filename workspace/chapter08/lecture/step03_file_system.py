import os
os.getcwd()
print('\n현재 경로', os.getcwd())
#작업 디렉터리 변경
os.chdir('../chapter08')
os.getcwd()
# 현재 작업 디렉터리  목록
os.listdir('.')
#디렉토리 생성
os.mkdir('test')
os.listdir('.')
#디렉토리 이동
os.chdir('test')
os.getcwd()
print('\n현재 경로', os.getcwd())
#여러 디렉터리 생성
os.makedirs('test2/test3')
os.listdir('.')
print(os.listdir('.'))
#디렉터리 이동
os.chdir('test2')
os.listdir('.')
#디렉터리 삭제
os.rmdir('test3')
os.listdir('.')
#상위 디렉터리 이동
os.chdir('../..')
os.getcwd()
#여러 개의 디렉터리 삭제
os.removedirs('test2/test2')

import os.path
os.getcwd()
print('\n현재 경로', os.getcwd())
os.chdir('../chapter08')
os.getcwd()

print(os.path.abspath('lecture/step01_try_except.py'))

os.path.dirname('lecture/step01_try_except.py')
os.path.exists('D:\\pywork\\workspace')
os.path.isfile('lecture/step01_try_except.py')

os.path.isdir('lecture')

os.path.split("c:\\test\\test1.txt")
os.path.join('c:\\test','test1.txt')

os.path.getsize('lecture/step01_try_except.py')