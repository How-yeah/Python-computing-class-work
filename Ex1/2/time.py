print('请输入时间（24 小时制，包含时、分、秒），以空格分开')
Time = input()
timeList = Time.split(' ')
hour = int(timeList[0])
minute = int(timeList[1])
second = int(timeList[2])
# hour = int(input('请输入时：'))
# minute = int(input('请输入分：'))
# second = int(input('请输入秒：'))

second = second + 1  # 获得下一秒时间
# 判断秒数进位
if second >= 60:
    second = second - 60
    minute = minute + 1
# 判断分钟数进位
if minute >= 60:
    minute = minute - 60
    hour = hour + 1
# 判断时钟数进位
if hour >= 24:
    hour = hour - 24
print(hour, '时', minute, '分', second, '秒')  # 输出结果
