import math
sum = 0
for k in range(0,3):
    coefficient_1 = 1103 + 26390 * k
    coefficient_2 = math.factorial(4*k)
    coefficient_3 = (math.factorial(k))**4
    coefficient_4 = 396**(4*k)
    mult = (coefficient_1 * coefficient_2) / (coefficient_3 * coefficient_4)
    sum = sum +mult
coefficient_5 = (2 * (2**0.5)) / 9801
pai = 1 / (sum * coefficient_5)
print(pai)
print(math.pi)
