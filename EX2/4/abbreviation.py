import copy

readFile = open('words.txt', 'r')
wordList = readFile.readlines()
for i in range(len(wordList)):
    wordList[i] = wordList[i][:-1]
wordDict = dict(zip(wordList, wordList))
readFile.close()


# def check(x):
#     if x == 'a' or x == 'i':
#         return True
#     if (check(x[1:]) in wordDict) or (check(x[:-1]) in wordDict):
#         return True
#     else:
#         return False


# def main():
res = []
for word in wordList:
    flag = True
    temp = word

    while temp != '':
        if temp == 'a' or temp == 'i':
            break
        if temp[1:] in wordDict or temp[1:] == 'a' or temp[1:] == 'i':
            temp = copy.deepcopy(temp[1:])
        elif temp[:1] in wordDict or temp[1:] == 'a' or temp[1:] == 'i':
            temp = copy.deepcopy(temp[:1])
        else:
            flag = False
            break

    if flag:
        print(word)
        res.append(word)


writeFile = open('result.txt', 'w')
for x in res:
    print(x, file=writeFile)
writeFile.close()


