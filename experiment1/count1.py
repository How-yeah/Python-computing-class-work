a_list = []
count = 0
with open(r'./experiment1/data/english.txt') as f:
    str1 = f.read()
a_list = str1.split(' ')
b_list = ['abc', 'rewq', 'lkj']
words_dict = dict(zip(a_list,a_list))
for i in b_list:
    if i in words_dict:
        count = count + 1
    print(i,':',count)
    count = 0
         