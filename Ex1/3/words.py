from time import time
start = time()
readFile = open('words.txt', 'r')
worldList = readFile.readlines()  # 将文件内单词存在列表中
readFile.close()
res = []
for word1 in worldList:
    word = word1[-2::-1]  # 获得原单词去掉回车符的逆序单词
    for word2 in worldList:  # 在列表中查找是否存在逆序单词
        if word == word2[:-1]:
            if word1 != word2 and (word2[:-1], word1[:-1]) not in res:  # 去除本身是回文串，以及重复的逆序对
                res.append((word1[:-1], word2[:-1]))
                print((word1[:-1], word2[:-1]))  # 输出结果
                break
end = time()
# 将结果输出到文件中.
writeFile = open('result.txt', 'w')
for x in res:
    print(x, file=writeFile)
print(end - start, file=writeFile)
writeFile.close()
