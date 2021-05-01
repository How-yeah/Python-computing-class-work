num = int(input("Input a number less than 1000: "))
if num == 1 or num == 0:
    print('{} = {} × {}'.format(str(num), str(num), str(num)))
    exit()
print(str(num) + ' = ', end='')

num_list = []
while num > 1:
    for i in range(2, num + 1):
        if num % i == 0:
            num_list.append(str(i))
            num //= i
            break

for i in range(len(num_list)):
    print(num_list[i], end=' x ' if i != len(num_list)-1 else '\n')
