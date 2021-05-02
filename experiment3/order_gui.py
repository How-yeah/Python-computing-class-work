from dearpygui.core import *
from dearpygui.simple import *
from order import *


def add_food(sender, data):
    food_name = get_value('_food_name')
    lunch.order(food_name)
    set_value('_food_name', '')
    set_value('order tip', 'ordered successfully!')


def show_food(sender, data):
    food_list = [food.name for food in lunch.result()]
    food_str = ''
    for food in food_list:
        food_str += food+'\n'
    set_value('show food', food_str)


with window("Which to Order?", autosize=True):
    lunch = Lunch()
    add_input_text('order food', source='_food_name')
    add_same_line()
    add_button('submit', callback=add_food)
    add_text('order tip', default_value=' ')
    add_separator()
    add_button('show menu', callback=show_food)
    add_text('show food', default_value=' ')


def main_callback(sender, data):
    if is_key_released(mvKey_Return):
        food_name = get_value('_food_name')
        lunch.order(food_name)
        set_value('_food_name', '')
        set_value('order tip', 'ordered successfully!')
    else:
        pass


set_render_callback(main_callback)
start_dearpygui()
