import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.listen()
screen.tracer(0)

my_turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(my_turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars(x_cor=300, y_cor=random.randint(-280, 250))
    car_manager.move_cars()

    if my_turtle.reset_turtle():
        scoreboard.increase_score()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(my_turtle) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()