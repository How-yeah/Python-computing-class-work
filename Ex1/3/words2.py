from time import time

start = time()
readFile = open('words.txt', 'r')
worldList = readFile.readlines()  # 将文件内单词存在列表中
wordDict = dict(zip(worldList, worldList))  # 将单词存入字典中
readFile.close()
res = []
for word1 in worldList:
    word = word1[-2::-1]  # 获得原单词去掉回车符的逆序单词
    word += '\n'
    if word in wordDict:  # 在字典中查找是否存在逆序单词
        res.append((word1[:-1], word[:-1]))
        print((word1[:-1], word[:-1]))  # 输出结果
end = time()
# 将结果输出到文件中.
writeFile = open('result2.txt', 'w')
for x in res:
    print(x, file=writeFile)
print(end - start, file=writeFile)
writeFile.close()
