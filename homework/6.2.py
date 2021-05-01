class Vecter:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, other):
        result = Vecter()
        result._x = self._x + other._x
        result._y = self._y + other._y
        result._z = self._z + other._z
        return result

    def __sub__(self, other):
        result = Vecter()
        result._x = self._x - other._x
        result._y = self._y - other._y
        result._z = self._z - other._z
        return result

    def __mul__(self, number):
        result = Vecter()
        result._x = self._x * number
        result._y = self._y * number
        result._z = self._z * number
        return result

    def __div__(self, number):
        result = Vecter()
        result._x = self._x / number
        result._y = self._y / number
        result._z = self._z / number
        return result
