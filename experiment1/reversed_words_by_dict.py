
import time

start = time.time()
with open(r'./experiment1/data/words.txt') as out_file:
    words = []
    for line in out_file:
        words.append(line.rstrip())
words_dict = dict(zip(words, words))  # 用字典包裹两个单词列表

reversed_words = []
count = 1
for word in words:
    rev_word = word[::-1]
    if rev_word in words_dict and rev_word != word:  # 在字典中查找是否存在逆序单词
        if rev_word + ' - ' + word not in reversed_words:
            reversed_words.append(word + ' - ' + rev_word)  # 将反序对存入列表
            print('find {} reversed words: {} - {}'.format(count, word, rev_word))
            count += 1
end = time.time()
print('耗时' + str(end-start) + '秒')
with open(r'./experiment1/data/reversed_words_by_dict.txt', 'w') as in_file:
    for word in reversed_words:
        in_file.write(word + '\n')
    print('写入完成!')
