import random

a = [random.randint(0, 100) for i in range(10)]
b = [random.randint(0, 100) for i in range(10)]

a.sort()
b.sort(reverse=True)
a.extend(b)

print(a)
