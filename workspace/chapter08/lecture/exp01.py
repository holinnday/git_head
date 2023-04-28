import os
file = open("D:/git_office/workspace/chapter08/data/ftest.txt", mode = 'r')

lines = file.readlines()
docs = []
words = []
for line in lines:
    docs.append(line.strip())
    for word in line.split():
        words.append(word)

print("문장 내용\n", docs)
print("문장 수\n", len(docs))
print("문장 내용\n", words)
print("문장 수\n", len(words))

