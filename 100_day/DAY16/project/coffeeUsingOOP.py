from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
m = Menu()
mm = MoneyMachine()
machine_flag = "on"
while machine_flag == "on":
    guess = input("What would you like to have? ({}) :".format(m.get_items())).lower()
    if guess=="off":
        break
    if guess == "report":
        cm.report()
        mm.report()
    else:
        item = m.find_drink(guess)
        flag = cm.is_resource_sufficient(item)
        if flag:  
            mm.make_payment(item.cost)
            cm.make_coffee(item)
