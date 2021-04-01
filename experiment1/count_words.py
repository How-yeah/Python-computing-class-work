import re
with open(r'./experiment1/english.txt') as out_file:
    contents = out_file.read()


def clear_nonwords(word):
    word = re.sub('\W+', '', word)
    return word


words_list = contents.split(' ', '')

dict = {}
for key in words_list:
    dict[key] = dict.get(key, 0) + 1  #查询键的值,若键不存在就新建，默认赋0值
# print(dict)
with open(r'./experiment1/frequency.txt', 'w') as in_file:
    for key, value in dict.items():
        in_file.write(key + ": " + value)
    print('写入完成!')
