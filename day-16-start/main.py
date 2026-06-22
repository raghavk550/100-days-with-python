# import turtle
#
# my_turtle = turtle.Turtle()
# my_screen = turtle.Screen()
#
# my_turtle.forward(100)
# my_turtle.color("red")
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.color("red", "green")
# my_turtle.left(90)
# my_turtle.forward(100)
#
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

# import prettytable
# my_table = prettytable.PrettyTable()
# my_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmender"])
# my_table.add_column("Type", ["Electric", "Water", "Fire"])
# print(my_table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
while is_machine_on:
    my_menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    user_choice = input(f"What would you like? ({my_menu.get_items()}): ")
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = my_menu.find_drink(user_choice)
        if item is not None:
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)
