import math
import random


def get_p(m: int, n: int) -> float:
    """
    班级中存在相同生日情况的概率
    :param m: 班级总个数
    :param n: 一个班级的人数
    :return: 概率
    """
    q = 0.0  # 存在相同生日情况的班级数
    for _class in range(m):
        same_birth = [False]*365  # 初始化一个班级成员的生日统计
        for _stu in range(n):
            birthday = random.randint(1, 365)
            if same_birth[birthday-1]:  # 找到相同生日的两个人
                q += 1
                break
            else:
                same_birth[birthday-1] = True  # 记录生日
    return q/m


if __name__ == '__main__':
    while True:
        class_num, stu_num = [int(x) for x in input(
            'input the number of classes and students: ').split()]
        p = get_p(class_num, stu_num)
        print("{}个班级, 每班{}人, 班级中存在相同生日情况的概率为{:.5%}".format(
            str(class_num), str(stu_num), p))
