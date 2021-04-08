a_list = []
count = 0
with open('experiment1/english.txt', encoding='utf-8') as f:
    str1 = f.read()
a_list = str1.split(' ')
b_list = ['abc', 'rewq', 'lkj']
for i in b_list:
    for j in a_list:
        if i == j:
            count = count + 1
    print(i,':',count)
    count = 0
         