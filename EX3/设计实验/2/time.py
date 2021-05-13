class Time:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        if not self.isValid():
            raise ValueError('时间不合法！')

    def __str__(self):
        timeStr = str(self.hour) + '时' + str(self.minute) + '分' + str(self.second) + '秒'
        return timeStr

    def __add__(self, other):
        if isinstance(other, Time):
            b = Time()
            b.hour = self.hour + other.hour
            b.minute = self.minute + other.minute
            b.second = self.second + other.second
            b.minute += b.second // 60
            b.second = b.second % 60
            b.hour += b.minute // 60
            b.minute = b.minute % 60
            b.hour = b.hour % 24
            return b
        else:
            print('Not Support')

    def time_to_int(self):
        second = self.hour * 3600 + self.minute * 60 + self.second
        return second

    def printTime(self):
        print(str(self))

    def is_a_after(self, other):
        if isinstance(other, Time):
            if self.time_to_int() < other.time_to_int():
                return True
            else:
                return False
        else:
            print('Not Support')

    def increment(self, n: int):
        second = (self.time_to_int() + n) % (24 * 3600)
        self.hour = second // 3600
        second %= 3600
        self.minute = second // 60
        second %= 60
        self.second = second

    def isValid(self):
        if 24 > self.hour >= 0 and 60 > self.minute >= 0 and 60 > self.second >= 0:
            return True
        else:
            return False


def main():
    try:
        t1 = Time(10, 30, 0)
        print(str(t1))
        t2 = Time(0, 31, 20)
        t2 = t2 + t1
        t2.printTime()
        print(t1.time_to_int())
        if t1.is_a_after(t2):
            print(str(t1) + '在' + str(t2) + '前')
        else:
            print(str(t1) + '在' + str(t2) + '后')
        t1.increment(10)
        t1.printTime()
        t3 = Time(30, 0, -1)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
