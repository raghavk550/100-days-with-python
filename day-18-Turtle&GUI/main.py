import random
from turtle import Turtle, Screen, colormode

# TKInter is responsible for GUI in python. Turtle module depends on this.

my_turtle = Turtle()
my_turtle.shape("arrow")
my_turtle.color("red")

colormode(255)

# Challenge 1

# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)

# Challenge 2

# for _ in range(10):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()
# my_turtle.forward(10)

# Challenge 3

# for i in range(3, 11):
#     for _ in range(i):
#         my_turtle.forward(100)
#         my_turtle.right(360 / i)

# Challenge 4

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# my_turtle.pensize(15)
my_turtle.speed("fastest")
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
#
# for _ in range(200):
#     # my_turtle.color(random.choice(colours))
#     my_turtle.color(random_color())
#     my_turtle.forward(30)
#     my_turtle.setheading(random.choice(directions))

# Challenge 5
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         my_turtle.color(random_color())
#         my_turtle.circle(100)
#         my_turtle.setheading(my_turtle.heading() + size_of_gap)
#
# draw_spirograph(10)
# my_turtle.setheading(90)
# my_turtle.penup()
# my_turtle.forward(100)
# my_turtle.pendown()
# draw_spirograph(10)

import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))
    # rgb_colors.append(color.rgb)

my_turtle.hideturtle()
my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

for _ in range(10):
    for _ in range(10):
        my_turtle.pendown()
        my_turtle.dot(10, random.choice(rgb_colors))
        my_turtle.penup()
        my_turtle.forward(50)
    my_turtle.penup()
    my_turtle.setheading(90)
    my_turtle.forward(50)
    my_turtle.setheading(180)
    my_turtle.forward(500)
    my_turtle.setheading(0)



my_screen = Screen()
my_screen.exitonclick()