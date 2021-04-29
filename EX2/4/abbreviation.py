from time import time

readFile = open('words.txt', 'r')
wordList = readFile.readlines()
for i in range(len(wordList)):
    wordList[i] = wordList[i][:-1]
wordSet = set(wordList)
wordSet.update({'a', 'i'})
readFile.close()


def check(Word):
    if Word in res:  # 若已在res中说明是可缩减单词，返回true
        return True
    if Word == 'a' or Word == 'i':  # 只剩一个字母且为'a'或'i'，满足条件，返回true
        return True
    for index in range(len(Word)):
        temp = Word[:index] + Word[index + 1:]  # 获得删去一个字母后的单词
        if temp in wordSet:
            return check(temp)  # 递归判断
    return False  # 删去任何位置都不在单词表中，返回false


def showProcess(Word, File):
    index = 0
    if Word == 'a' or Word == 'i':
        print(Word)
        print(Word, file=File)
    for ch in Word:
        temp = Word[:index] + Word[index + 1:]
        if temp in wordSet:
            print(Word, '->', end='')
            print(Word, '->', file=File, end='')
            return showProcess(temp, File)
        index += 1


start = time()
res = set()
for word in wordList:
    flag = True
    flag = check(word)
    if flag:
        print(word)
        res.add(word)
end = time()

print(end - start)
writeFile = open('result.txt', 'w')
for x in res:
    print(x, file=writeFile)
print(end - start, file=writeFile)
maxLenWord = ''
for x in res:
    if len(x) > len(maxLenWord):
        maxLenWord = x
print("最长单词是：", maxLenWord)
showProcess(maxLenWord, writeFile)
writeFile.close()
