class Time():
    def __init__(self, hour: int, minute: int, second: int):
        self._hour: int = hour
        self._minute: int = minute
        self._second: int = second

    def __str__(self):
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self._hour, self._minute, self._second)

    def __int__(self):
        return 3600*self._hour+60*self._minute+self._second

    def __add__(self, other_time):
        seconds = int(self)+int(other_time)
        return Time(seconds//3600, (seconds//60) % 60, seconds % 60)

    def __gt__(self, other_time) -> bool:
        # greater than
        return int(self) > int(other_time)

    def __lt__(self, other_time) -> bool:
        # less than
        return int(self) < int(other_time)

    def __le__(self, other_time):
        # less or equal
        return int(self) <= int(other_time)

    def __ge__(self, other_time):
        # greater or equal
        return int(self) >= int(other_time)

    def time2int(self) -> int:
        return int(self)

    def printtime(self):
        print(self)

    def isafter(self, other_time):
        return self > other_time
        return Time(seconds//3600, (seconds//60) % 60, seconds % 60)

    def increment(self, n: int):
        seconds = int(self)+n
        return Time(seconds//3600, (seconds//60) % 60, seconds % 60)

    def isvalid(self):
        return 0 <= self._hour < 24 and 0 <= self._second < 60 and 0 <= self._second < 60


if __name__ == "__main__":
    a = Time(2, 14, 59)
    b = Time(3, 20, 30)
    c = Time(100, 100, 100)
    print(a, b)
    print(a.isafter(b))
    print(a.increment(1))
    print(c.isvalid())
