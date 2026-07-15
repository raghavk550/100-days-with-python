try:
    file = open("my_file.txt")
    my_dict = {"key": "value"}
    print(my_dict["key"])
except FileNotFoundError:
    file = open("my_file.txt", "w")
    file.write("something")
except KeyError as e:
    print(f"The key {e} does not exist")
else:
    content = file.read()
    print(content)
finally:
    # Raise your own error
    raise KeyError("My error")