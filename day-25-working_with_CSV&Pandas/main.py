# try:
#     with open("weather_data.csv", "r") as file:
#         data = file.read().splitlines()
#         print(data)
# except:
#     print("File not found")

# import csv
#
# try:
#     with open("weather_data.csv", "r") as file:
#         data = csv.reader(file)
#         temperatures = []
#         for index, row in enumerate(data):
#             if index != 0:
#                 temperatures.append(int(row[1]))
#             print(row)
#         print(temperatures)
# except:
#     print("File not found")

import pandas
import time
from pandas._libs.tslibs.offsets import Nano
from pandas.core.arrays.categorical import contains

# data = pandas.read_csv("weather_data.csv")

"""
We have DataFrames (which is 2D) and Series (which is 1D) in pandas
Ex = data here is DataFrame while data["temp"] is the Series - (single column or list) 
where temp is the column name
"""
# print(data)
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
# print(data["temp"].mean())
# print(data["temp"].max())

""" We can get the row as well """
# print(data[data["temp"] == 22])

# max = data["temp"].max()
# print(data[data["temp"] == max])

# monday = data[data["day"] == "Monday"]
# monday_temp = monday["temp"]
# print((monday_temp * (9 / 5)) + 32)

""" Create DataFrame from scratch """
# data_dict = {
#     "students" : ["Amy", "James", "Rk"],
#     "scores" : [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
#
# """ we can create csv file as well """
# new_data.to_csv("new_data.csv")

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# colors = data["Primary Fur Color"].dropna().to_dict()
# data_dict = {
#     "Color" : [],
#     "Count" : []
# }
# for color_keys in colors.keys():
#     color = colors[color_keys]
#     if type(color) is str:
#         if color in data_dict["Color"]:
#             index = data_dict["Color"].index(color)
#             data_dict["Count"][index] += 1
#         else:
#             data_dict["Color"].append(color)
#             data_dict["Count"].append(1)
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("Squirrel_Count.csv")

from turtle import Turtle, Screen

my_screen = Screen()
# my_screen.addshape("blank_states_img.gif")
my_screen.bgpic("blank_states_img.gif")

my_turtle = Turtle()
# my_turtle.shape("blank_states_img.gif")
my_turtle.penup()
my_turtle.hideturtle()

"""
Method to get the x and y coordinates on click of screen 
# def get_mouse_click_coord(x_cor: float, y_cor: float):
#     print(x_cor, y_cor)
# 
# my_screen.onscreenclick(get_mouse_click_coord)
# my_screen.mainloop() -> Alternative of my_screen.exitonclick()
"""

data = pandas.read_csv("50_states.csv")
total_data_len = len(data)
my_score = 0

is_game_on = True
is_guessed = False
states_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < total_data_len:
    prompt =  "What's another state name?" if is_guessed else "What's first state name?"
    is_guessed = True
    user_ans = my_screen.textinput(f"{my_score}/{total_data_len} States Correct", prompt).title()
    if user_ans in states_list:
        guessed_states.append(user_ans)
        current_data = data[data["state"] == user_ans]
        x = int(current_data["x"].item())
        y = int(current_data["y"].item())
        my_turtle.goto(x, y)
        my_turtle.write(user_ans, align="center", font=("Arial", 8, "normal"))
        my_score += 1
        time.sleep(0.4)

my_screen.exitonclick()