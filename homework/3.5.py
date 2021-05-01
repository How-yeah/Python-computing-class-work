import random

a = [random.randint(0, 100) for i in range(20)]

a_even = a[::2]
a_even.sort(reverse=True)
a[::2] = a_even

print(a)
