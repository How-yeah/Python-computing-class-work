f = open('text.txt', 'r')
res = dict()  # 使用字典类型存储结果，单词为键，频率为值
for line in f.readlines():
    wordlist = line.split(' ')  # 将字符串按空格分开成单词
    for word in wordlist:
        word = word.lower()  # 将所有单词改为小写
        if word.isalpha():
            res[word] = res.get(word, 0) + 1  # 对该单词出现出现频率+1
f.close()
# 结果输出到文件
f = open('WordCount.txt', 'w')
for x in res:
    print(x, ':', res[x], file=f)
f.close()
