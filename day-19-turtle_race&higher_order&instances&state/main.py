import random
import turtle

# my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

"""
Etch a sketch
"""
# def move_forward():
#     my_turtle.forward(10)
#
# def move_backward():
#     my_turtle.backward(10)
#
# def turn_left():
#     my_turtle.setheading(my_turtle.heading() + 10)
#
# def turn_right():
#     my_turtle.setheading(my_turtle.heading() - 10)
#
# def clear_screen():
#     my_turtle.clear()
#     my_turtle.penup()
#     my_turtle.home()
#     my_turtle.pendown()
#
# # Screen Listener
# my_screen.listen()
# my_screen.onkey(move_forward, "w") #-> This is the higher order function as it takes another
# # function as input and working with that.
# my_screen.onkey(move_backward, "s")
# my_screen.onkey(turn_left, "a")
# my_screen.onkey(turn_right, "d")
# my_screen.onkey(clear_screen, "c")

"""
Turtle Race
"""

# Setup screen frame for Coordinate System
is_race_on = False
my_screen.setup(500, 400)
user_choice = my_screen.textinput("Make your bet", "Who will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yCor = -70
all_turtle = []
for index in range(0, len(colors)):
    tim = turtle.Turtle()
    tim.color(colors[index])
    tim.shape("turtle")
    tim.penup()
    tim.goto(-230, yCor)
    yCor = yCor + 30
    all_turtle.append(tim)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
        distance = random.randint(0, 10)
        turtle.forward(distance)




my_screen.exitonclick()
