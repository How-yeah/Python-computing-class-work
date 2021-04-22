from time import time

readFile = open('words.txt', 'r')
wordList = readFile.readlines()
for i in range(len(wordList)):
    wordList[i] = wordList[i][:-1]
wordDict = set(wordList)
wordDict.update({'a', 'i'})
readFile.close()


def check(Word):
    if Word in res:
        return True
    if Word == 'a' or Word == 'i':
        return True
    for index in range(len(Word)):
        temp = Word[:index] + Word[index + 1:]
        if temp in wordDict:
            return check(temp)
    return False


def showProcess(Word):
    index = 0
    if Word == 'a' or Word == 'i':
        print(Word)
    for ch in Word:
        temp = Word[:index] + Word[index + 1:]
        if temp in wordDict:
            print(Word, '->', end='')
            return showProcess(temp)
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
showProcess(maxLenWord)
writeFile.close()
