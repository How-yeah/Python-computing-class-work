import math

c = 2 * (2 ** 0.5) / 9801
Pi = 0.0
print('k值', '\t', '计算结果（15位）', '\t\t', 'Math库结果（15位）', '\t\t', '差值（精确到20位）')
for k in range(1, 10):
    Pi = 0.0
    for i in range(k):
        Pi += (math.factorial(4 * i) * (1103 + 26390 * i)) / ((math.factorial(i) ** 4) * (396 ** (4 * i)))
    Pi *= c
    Pi = 1.0 / Pi
    print(k, '\t', '%.15lf' % Pi, '\t\t', math.pi, '\t\t', '%.20lf' % abs(Pi - math.pi))
