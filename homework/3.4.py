import random

a = [random.randint(0, 100) for i in range(50)]

for i in range(len(a)-1, -1, -1):
    if a[i] % 2 == 1:
        del a[i]

print(a)
