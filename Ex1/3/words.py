readFile = open('words.txt', 'r')
worldList = readFile.readlines()  # 将文件内单词存在列表中
readFile.close()
res = []
for word1 in worldList:
    word = word1[-2::-1]  # 获得原单词去掉回车符的逆序单词
    for word2 in worldList:  # 在列表中查找是否存在逆序单词
        if word == word2[:-1]:
            res.append((word1[:-1], word2[:-1]))
            print((word1[:-1], word2[:-1]))  # 输出结果
            break
# 将结果输出到文件中
writeFile = open('result.txt', 'w')
for x in res:
    print(x, file=writeFile)
writeFile.close()
