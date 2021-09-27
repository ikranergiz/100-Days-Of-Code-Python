from menu import Menu ,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()

while True:
    order = input(my_menu.get_items())

    if order == "report":
        my_coffee_maker.report()

    elif my_menu.find_drink(order):
        coffee_item = my_menu.find_drink(order)  # find_drink fonksiyonu MenuItem nesnesi döndürüyor

        if my_coffee_maker.is_resource_sufficient(coffee_item):
            my_money_machine.make_payment(coffee_item.cost)
            my_coffee_maker.make_coffee(coffee_item)











