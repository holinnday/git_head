from re import findall, sub

texts = ['우리나라 대한민국, 우리나라%$ 만세', ' 비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

#영문 소문자로 변경
texts_rel = [t.lower() for t in texts]
print('texts_rel :', texts_rel)

#숫자 제거
texts_re2 = [sub("[0-9]", '', text) for text in texts_rel]
print('texts_re2 :', texts_re2)

#문장 부호 제거
texts_re3 = [sub('[,.?!:;]', '', text) for text in texts_re2]
print('texts_re3 :', texts_re3)

# 특수문자 제거
spec_str = '[@#$%^&*()]'
texts_re4 = [sub(spec_str, '', text) for text in texts_re3]
print('texts_re4 :', texts_re4)

#영문자 제거
texts_re5 = [''.join(findall("[^a-z]", text)) for text in texts_re4]
print('texts_re5 :', texts_re5)

#공백 제거
texts_re6 = [' '.join(text.split()) for text in texts_re5] #공백 기준 split -> join 결합
print('texts_re6 :', texts_re6)