with open(r'./experiment1/data/words.txt') as out_file:
    words = []
    for line in out_file:
        words.append(line.rstrip())
reversed_words = []
count = 1
for word_x in words:
    for word_y in words:
        if word_x[::-1] == word_y and word_x != word_y:
            if word_y + " - " + word_x not in reversed_words:
                print('find {} reversed words: {} - {}'.format(count, word_x, word_y))
                count += 1
                reversed_words.append(word_x + " - " + word_y)
with open(r'./experiment1/reversed_words.txt', 'w') as in_file:
    for word in reversed_words:
        in_file.write(word + '\n')
    print('写入完成!')
