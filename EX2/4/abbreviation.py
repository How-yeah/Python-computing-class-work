from time import time

readFile = open('words.txt', 'r')
wordList = readFile.readlines()
for i in range(len(wordList)):
    wordList[i] = wordList[i][:-1]
wordDict = set(wordList)
wordDict.update({'a', 'i'})
readFile.close()


def check(words):
    if words in res:
        return True
    if words == 'a' or words == 'i':
        return True
    for index in range(len(words)):
        temp = words[:index] + words[index + 1:]
        if temp in wordDict:
            return check(temp)
    return False


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
writeFile.close()
