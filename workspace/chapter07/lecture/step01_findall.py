from re import findall

st1 = '1234 abc홍길도 ABC_555_6 이사도시'

print(findall('1234', st1))
print(findall('[0-9]', st1)) #모든 숫자를 찾아라, [A-Z] 모든 대문자 알파벳을 찾아라
print(findall('[0-9]{3}', st1)) # 세번만 연속되는 숫자를 찾아라
print(findall('[0-9]{3,}', st1)) # 세번 이상 연속되는 숫자를 찾아라
print(findall('\\d{3,}', st1)) # 세번이상 연속되는 숫자(\\d)를 찾아라

#문자열 찾기
print(findall('[가-힣]{3,}', st1)) #세번 이상 연속되는 문자열을 찾아라
print(findall('[a-z]{3}', st1)) #세번만 연속되는 영어 소문자를 찾아라
print(findall('[a-z|A-Z]{3}', st1)) #영어 대문자 혹은(or) 소문자 중에서 세번만 연속되는 문자열을 찾아라

#특정 위치의 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'

print(findall('^test', st2)) #test로 시작하는 문자열
print(findall('st$', st2)) #st로 끝나는 문자열 (끝나는것만 가져오기)

print(findall('.bc', st2)) #bc로 끝나는 문자열

print(findall('t.',st2)) # t로 시작하는 문자열

#단어 찾기  - 한글+영문+숫자
st3 = 'test^홍길동 acb 대한*민국 123$bc'
words = findall('\\w{3,}', st3) #문자 3자 이상
print(words)

print(findall('[^^*$]+', st3) #특수문자 제외 