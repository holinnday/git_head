import os
from glob import glob

print(os.getcwd())
img_path = '../../chapter08/images/'
img_path2 = '../../chapter08/images2/' # 경로 지정

if os.path.exists(img_path):
    print('해당 디텍터리가 존재함')
    images = []
    os.mkdir(img_path2)

    for pic_path in glob(img_path + '*.png'):

        img_path = os.path.split(pic_path)
        images.append(img_path[1])

        rfile = open(file=pic_path, mode='rb')
        output = rfile.read()

        wfile = open(img_path2+img_path[1], mode='wb')
        wfile.write(output)
    rfile.close(); wfile.close()
else:
    print('해당 디렉터리가 없음')

print('png file=', images)
