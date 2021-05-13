class Food:
    def __init__(self, name: str = ''):
        self.foodName = name

    def __str__(self):
        return self.foodName


class Employee(object):
    def __init__(self, name: str = ''):
        self.__employName = name
        self.menu = []

    @property
    def name(self):
        return self.__employName

    def setMenu(self, menu):
        self.menu = menu

    def showMenu(self):
        return self.menu

    def takeOrder(self, foodName):
        if foodName in self.menu:
            return Food(foodName)
        else:
            raise ValueError('Food is not exist!')


class Custom(object):
    def __init__(self, name: str = ''):
        self.__customName = name
        self.foodList = []

    @property
    def name(self):
        return self.__customName

    def placeOrder(self, employee: Employee, foodName):
        try:
            self.foodList.append(employee.takeOrder(foodName))
        except ValueError as e:
            print(e)

    def showOrder(self):
        return self.foodList


class Lunch:
    def __init__(self, custom: Custom, employee: Employee):
        self.custom = custom
        self.employee = employee

    def order(self, foodName):
        self.custom.placeOrder(self.employee, foodName)

    def result(self):
        return self.custom.showOrder()

