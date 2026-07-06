"""
List comprehension -
new_list = [new_item for item in list]

Conditional List comprehension -
new_list = [new_item for item in list if test]

Dict comprehension -
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key, value) in dict.items()}

Conditional Dict comprehension -
new_dict = {new_key:new_value for (key, value) in dict.items() if test}
"""

# numbers = [1,2,3]
# new_list = [num + 1 for num in numbers]
#
# doubled_list = [num * 2 for num in range(1,5)]
# print(doubled_list)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {key: round((value * (9 / 5) + 32), 2) for (key, value) in weather_c.items()}
#
# print(weather_f)

import pandas

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {value["letter"]:value["code"] for (index, value) in alphabet_data_frame.iterrows()}
user_name = input("Enter your name: ")

result = [alphabet_dict[char.title()] for char in user_name]
print(result)