class Food():
    def __init__(self, name):
        self.name = name


class Employee():
    def take_order(self, food_name):
        return Food(food_name)


class Customer():
    def __init__(self):
        self.food_list = []

    def place_order(self, employee, food_name):
        self.food_list.append(employee.take_order(food_name))

    def show_food(self):
        return self.food_list


class Lunch():
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, food_name):
        self.customer.place_order(self.employee, food_name)

    def result(self):
        return self.customer.show_food()


if __name__ == '__main__':
    x = Lunch()
    x.order('burritos')
    x.result()
    x.order('pizza')
    x.result()
