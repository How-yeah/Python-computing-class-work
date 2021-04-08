hour=int(input('输入时：'))
mintue=int(input('输入分：'))
second=int(input('输入秒'))
print('当前时间：',hour,':',mintue,':',second)
if hour==23 and mintue==59 and second==59:
    print("1秒后的时间：00：00：00")
else:
    if second==59:
        if mintue==59:
            hour=hour+1
            mintue=00
            second=00
        else:
            mintue=mintue+1
            second=00
    else:
        second=second+1
    print("1秒后的时间：",hour,':',mintue,':',second)

