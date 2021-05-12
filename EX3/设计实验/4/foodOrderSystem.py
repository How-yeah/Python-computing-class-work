from foodOrderClass import *
import tkinter as tk
from tkinter import ttk


# 点餐程序及界面
def foodOrder(customName, employeeName, window):
    # 创建相应对象
    custom = Custom(customName)
    employee = Employee(employeeName)
    lunch = Lunch(custom, employee)
    KFCMenu = ['hamburger', 'sandwiches', 'French Fries']
    Pizza_hutMenu = ['fish pizza', 'beef pizza']
    if employee.name == 'KFC':
        employee.setMenu(KFCMenu)
    if employee.name == 'Pizza hut':
        employee.setMenu(Pizza_hutMenu)

    # 关闭上一个页面，创建新页面
    window.destroy()
    window = tk.Tk()
    window.title('Order System')
    window.geometry('800x600')

    title = tk.Label(window, text='Place order your food!', font=('Arial', 14))
    title.pack()

    # 构造菜单的CheckButton
    menu = []
    menu_v = []
    opt = []
    for i, food in enumerate(employee.showMenu()):
        menu_v.append(tk.StringVar())
        off_value = 0
        menu.append(tk.Checkbutton(window, text=food, onvalue=food, offvalue=off_value, variable=menu_v[i]))
        menu[i].place(x=350, y=120 + 50 * i)
        opt.append(off_value)
        menu[-1].deselect()

    def submitMenu():
        for ix, item in enumerate(menu):
            opt[ix] = (menu_v[ix].get())
        # print(employee.showMenu())
        for x in opt:
            # print(x)
            if x != '0':
                lunch.order(x)
        result = lunch.result()
        for index in range(len(result)):
            result[index] = str(result[index])
        print(result)

        # 创建新的页面
        listWindow = tk.Tk()
        listWindow.title('Food List')
        listWindow.geometry('300x500')

        foodListTitle = tk.Label(listWindow, text=custom.name + ' your food list', font=('Arial', 14))
        foodListTitle.pack()

        # 构建订单label
        foodList = []
        index = 0
        for x in result:
            foodList.append(tk.Label(listWindow, text=x, font=('Arial', 11)))
            foodList[index].place(x=100, y=100 + 40 * index)
            index += 1

        listWindow.mainloop()

    submitButton = tk.Button(window, text='Submit', command=submitMenu, width=30)
    submitButton.place(x=300, y=350)

    window.mainloop()


def main():
    # 主程序框架
    window = tk.Tk()
    window.title('Order System')
    window.geometry('800x600')
    title = tk.Label(window, text='Food Order System', font=('Arial', 14))
    title.pack()

    # 用户名输入
    tk.Label(window, text='User name:').place(x=200, y=200)
    userName = tk.StringVar()
    userName.set('')
    entry_userName = tk.Entry(window, textvariable=userName, font=('Arial', 14))
    entry_userName.place(x=300, y=200)

    # 餐厅选择
    tk.Label(window, text='Restaurant:').place(x=200, y=260)
    restaurant = tk.StringVar()
    restaurantList = ttk.Combobox(window, textvariable=restaurant)
    restaurantList["values"] = ('place choose restaurant', 'KFC', 'Pizza hut')
    restaurantList.current(0)
    restaurantList.place(x=320, y=260)

    # 进入点餐程序
    def starOrder():
        customName = userName.get()
        employeeName = restaurant.get()
        foodOrder(customName, employeeName, window)

    button_start = tk.Button(window, text='Stat to Order', command=starOrder)
    button_start.place(x=350, y=400)

    window.mainloop()


if __name__ == '__main__':
    main()
