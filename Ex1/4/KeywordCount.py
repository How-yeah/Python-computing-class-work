keywordList = ['python', 'java', 'an', 'is', 'elegant']
f = open('text.txt', 'r')
res = dict()
for key in keywordList:
    res[key] = res.get(key, 0)
for line in f.readlines():
    wordlist = line.split(' ')
    for word in wordlist:
        word = word.lower()
        if word.isalpha():
            if word in res:
                res[word] = res.get(word, 0) + 1
f.close()
f = open('KeywordCount.txt', 'w')
# print(res, file=f)
for x in res:
    print(x, ':', res[x], file=f)
f.close()
