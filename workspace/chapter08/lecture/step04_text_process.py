import os

# 텍스트 디렉터리 경로 지정
print(os.getcwd())
txt_data = '../../chapter08/txt_data/' #데이터 파일을 가져오기 위해 상대 경로 지정

# 텍스트 디렉터리 목록 반환
sub_dir = os.listdir(txt_data)
print(sub_dir)

# 각 디렉터리의 텍스트 자료 수집 함수
def textPro(sub_dir) :
    first_txt = []
    second_txt = []

    #디렉터리 구성
    for sdir in sub_dir :
        dirname = txt_data + sdir
        file_list = os.listdir(dirname) #파일 목록 반환

        for fname in file_list:
            file_path = dirname + '/' + fname

            if os.path.isfile(file_path) :
                try :
                    # 텍스트 자료 수집
                    file = open(file_path, 'r')
                    if sdir == 'first':
                        first_txt.append(file.read())
                    else :
                        second_txt.append(file.read())
                except Exception as e:
                    print('예외발생 :', e)
                finally:
                    file.close()
    return first_txt, second_txt

first_txt, second_txt = textPro(sub_dir)

print('first_tex 길이 =', len(first_txt))
print('second_tex 길이 =', len(second_txt))

tot_texts = first_txt + second_txt
print('tot_texts 길이=', len(tot_texts))

print(tot_texts)
print(type(tot_texts))

import pickle

print(os.getcwd())

pfile_w = open("../../chapter08/data/tot_texts.pck", mode='wb')
pickle.dump(tot_texts, pfile_w)

# file 불러오기
pfile_r = open("../../chapter08/data/tot_texts.pck", mode='rb')
tot_texts_read = pickle.load(pfile_r)
print('tot_texts 길이=', len(tot_texts_read))

print(type(tot_texts_read))
print(tot_texts_read)

