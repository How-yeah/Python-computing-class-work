while True:
    import random
    m = int(input('班级数: '))
    n = int(input('每个班级的人数: '))
    q = 0
    for _class in range(m):
        same_birthday = [False] * 365
        for stu in range(n):
            birth = random.randint(1,365)
            if same_birthday[birth-1]:
                q +=1
                break
            else:
                same_birthday[birth-1] = True
    p = q / m
    print(p)