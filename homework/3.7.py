# method 1
odd_sum = 0
for i in range(1, 100, 2):
    odd_sum += i
print('The odd sum is ' + str(odd_sum))

# method 2
odd_sum = 0
num = 100
while num > 0:
    if num % 2 == 1:
        odd_sum += num
    num -= 1

print('The odd sum is ' + str(odd_sum))
