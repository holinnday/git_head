from re import findall, sub

texts = ['AFAB54747,adabag?', 'abTTA $$;a12:2424.', 'uysfsfA,A124&***$?']

def  clean_text(text) :
    texts_re = text.lower()
    texts_re2 = sub("[0-9]", '', texts_re) #숫자제거
    texts_re3 = sub('[,.?!:;]', '', texts_re2) #문장부호 제거
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3) #특수문자 제거
    texts_re5 = sub(' ', '', texts_re4)
    return texts_re5

texts_result = [clean_text(text) for text in texts]
print(texts_result)

