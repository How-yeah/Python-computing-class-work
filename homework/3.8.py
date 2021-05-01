num = [1, 2, 3, 4]
num_all = []
for i in range(0, len(num)):
    num[i], num[0] = num[0], num[i]
    for j in range(1, len(num)):
        num[j], num[1] = num[1], num[j]
        for k in range(2, len(num)):
            num[k], num[2] = num[2], num[k]
            num_all.append(int(str(
                num[0]) + str(num[1]) + str(num[2]) + str(num[3])))
            num[k], num[2] = num[2], num[k]
        num[j], num[1] = num[1], num[j]
    num[i], num[0] = num[0], num[i]

result = []
for number in num_all:
    for i in range(2, number):
        if not number % i:
            break
    else:
        result.append(number)

print("The result is: ", end="")
for number in result:
    print(number, end=" ")
