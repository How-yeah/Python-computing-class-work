input_list = eval(input('Input a list: '))
a, b = input('input start and end: ').split(',')

print('The sub list is: ', end='')
print(input_list[int(a): int(b)+1])
