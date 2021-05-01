dict_a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
while True:
    input_key = input('请输入键名: ')
    value = dict_a.get(input_key, '您输入的键不存在!')
    if value != '您输入的键不存在!':
        print('其值为: ', end='')
    print(value)
