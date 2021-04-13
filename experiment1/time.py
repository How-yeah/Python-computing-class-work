hour = int(input('输入时：'))
mintue = int(input('输入分：'))
second = int(input('输入秒: '))
if (hour < 0 or hour > 23) or (mintue < 0 or mintue > 59) or (second < 0 or second > 59):
    print('输入溢出')
else:
    print('当前时间：', hour, ': ', mintue, ': ', second)
    if hour == 23 and mintue == 59 and second == 59:
        print("1秒后的时间：00 ：00 ：00")
    else:
        if second == 59:
            if mintue == 59:
                hour = hour+1
                mintue = 00
                second = 00
            else:
                mintue = mintue+1
                second = 00
        else:
            second = second+1
        print("1秒后的时间：", hour, ': ', mintue, ': ', second)
