from turtle import Screen
import time

from scoreboard import Scoreboard
from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.update()

screen.listen()
screen.onkey(snake.move_snake_up, "Up")
screen.onkey(snake.move_snake_down, "Down")
screen.onkey(snake.move_snake_left, "Left")
screen.onkey(snake.move_snake_right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.create_food()
        score.increase_score()
        snake.increase_segment()

    if (snake.segments[0].xcor() > 280
            or snake.segments[0].xcor() < -299
            or snake.segments[0].ycor() > 299
            or snake.segments[0].ycor() < -299):
        # is_game_on = False
        # score.game_over()
        score.reset_score()
        snake.reset_snake()

    for segment in snake.segments[1:]: # <- Here, we have done slicing
        if snake.segments[0].distance(segment) < 10:
            """
            Here instead of using if-else, we can use the slicing
            Slicing can be used with both lists and tuples.
            Params are start, end and step
            
            Ex - list = [1,2,3,4,5,6,7]
            print(list[2:5]) -> [3,4,5]
            print(list[1:]) -> [2,3,4,5,6,7]
            print(list[:2]) -> [1,2,3]
            print(list[:2:2]) -> [1,3]
            """
            if snake.segments[0] == segment:
                pass
            else:
                # is_game_on = False
                # score.game_over()
                score.reset_score()
                snake.reset_snake()

screen.exitonclick()

# class Animal:
#     def __init__(self):
#         self.num_of_eyes = 2
#
#     def take_breathe(self):
#         print("Breathe")
#
# class Fish(Animal):
#     def __init__(self):
#         self.wings = 2
#         super().__init__()
#
#     def swim(self):
#         print("Swim")
#
# fish = Fish()
# print(fish.wings)
# print(fish.num_of_eyes)
# fish.take_breathe()
# fish.swim()
