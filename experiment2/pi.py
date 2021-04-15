import math


coef = 2 * 2 ** 0.5 / 9801  # 系数
sum_ = 0  # 累加
print('|{:^8}|{:^24}|{:^24}|{:^24}|'.format(
    'count', 'result', 'math.pi', 'error'))
for i in range(4):
    top = math.factorial(4 * i) * (1103 + 26390 * i)  # 分子
    bottom = math.factorial(i) ** 4 * 396 ** (4 * i)  # 分母
    one_piece = coef * top / bottom  # 一项
    sum_ += one_piece
    print('|{:^8}|{:^24.20f}|{:^24.20f}|{:^24.20f}|'.format(
        i, 1 / sum_, math.pi, abs(1 / sum_ - math.pi)))
    if one_piece < 1e-20:
        break
