import json
import tkinter
from tkinter import messagebox
import pyperclip

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

def search_pressed():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            data_dict = data[website_entry.get()]
            email = data_dict["email"]
            password = data_dict["password"]
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {email}"
                                                                   f"\nPassword: {password}")
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("JSONDecodeError")
    except KeyError as error:
        print(f"The key {error} was not found.")

def generate_password():
    password_entry.delete(0, tkinter.END)
    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    """
    or
    """
    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0, password)

def add_button_pressed():
    if website_entry.get() != "" and email_entry.get() != "" and password_entry.get() != "":
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: "
                                                               f"\nEmail: {email_entry.get()}"
                                                               f"\nPassword: {password_entry.get()}"
                                                               f"\nIs it ok to save?")
        if is_ok:
            new_data = {
                website_entry.get(): {
                    "email": email_entry.get(),
                    "password": password_entry.get(),
                }
            }
            try:
                with open("data.json", "r") as file:
                    # Write data to json file
                    # json.dump(new_data, file, indent=4)

                    # Reading old data
                    data = json.load(file)
            except FileNotFoundError, json.JSONDecodeError:
                data = {}

            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # writing new data into the file
                json.dump(data, file, indent=4)

                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
    elif website_entry.get() == "":
        messagebox.showerror(title="Error", message="Website cannot be empty")
    elif email_entry.get() == "":
        messagebox.showerror(title="Error", message="Email cannot be empty")
    elif password_entry.get() == "":
        messagebox.showerror(title="Error", message="Password cannot be empty")

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
canvas.grid(row=0, column=1)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry()
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="w", padx=10)

search_button = tkinter.Button(text="Search", command=search_pressed)
search_button.grid(row=1, column=2, padx=10, sticky="we")

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = tkinter.Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="we", padx=10)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(justify="left")
password_entry.grid(row=3, column=1, sticky="w", padx=10)

gen_password_button = tkinter.Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2, padx=10)

add_button = tkinter.Button(text="Add", command=add_button_pressed)
add_button.grid(row=4, column=1, columnspan=2, padx=10, sticky="we")

window.mainloop()