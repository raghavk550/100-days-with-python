# import tkinter
#
# window = tkinter.Tk()
#
# window.title("My first GUI program")
# window.minsize(500, 300)
# window.config(padx=20, pady=20)
#
# # Label
# my_label = tkinter.Label(text="My first GUI program", font=("Arial", 24, "bold"))
# # my_label["text"] = "My second GUI program"
# # my_label.config(text="New Text")
# # my_label.pack() # Need to display on the screen
# # my_label.place(x=0, y=0) # Another way to display on screen
# my_label.grid(row=0, column=0)
#
# # Button
# def button_clicked():
#     my_label["text"] = "Button Clicked"
#     if input.get() != "":
#         my_label["text"] = f"{input.get()}"
#
# my_button = tkinter.Button(text="Click me", command=button_clicked)
# # my_button.pack()
# my_button.grid(row=1, column=1)
#
# def new_button_clicked():
#     print("New Button Clicked")
#
# new_button = tkinter.Button(text="Click me", command=new_button_clicked)
# # my_button.pack()
# new_button.grid(row=0, column=2)
#
# # Entry
# input = tkinter.Entry()
# # input.pack()
# input.grid(row=2, column=3)
#
#
# window.mainloop()

import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input = tkinter.Entry(width=10)
input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

km_result_label = tkinter.Label(text="0")
km_result_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

def new_button_clicked():
    if input.get() != "" and float(input.get()) != None:
        result = float(input.get()) * 1.609
        km_result_label.config(text=str(int(result)))


calculate_button = tkinter.Button(text="Calculate", command=new_button_clicked)
calculate_button.grid(row=2, column=1)

window.mainloop()