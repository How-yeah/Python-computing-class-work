import time
start = time.time()

a_list=[]
b_list=[]
with open(r'./experiment1/data/words.txt') as f:
	for line in f:
		a_list.append(line.strip('\n').split(',')[0])
words_dict = dict(zip(a_list,a_list))

count = 1
for word in a_list:
    rev_word=word[::-1]
    if rev_word in words_dict and rev_word != word and rev_word + '-' + word not in b_list: 
        b_list.append(word + '-' + rev_word)
        print(word, '-' , rev_word ,';')
        count = count + 1
end = time.time()
print('耗时' + str(end-start) + '秒')
print(count)




